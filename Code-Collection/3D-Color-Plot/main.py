import argparse

import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

# =====================================================================
# Academic font styling (serif / Computer Modern family)
# =====================================================================
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Computer Modern Roman', 'CMU Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'cm',
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.titlesize': 15,
})


# =====================================================================
# Global color mapping (warm palette, 10 colors)
#
# Keys   : color hex codes (warm tones from dark to light)
# Values : (lower_bound, upper_bound) — the interval of function
#           values that map to that color.
#
# Convention:
#   - 1 negative interval  (covers all V < 0)
#   - 9 positive intervals (covers V >= 0 upward)
#
# Both run_default() and run_spherical() use this mapping.
# Adjust the interval boundaries to match the function value range
# printed at runtime.
# =====================================================================
COLOR_MAPPING = {
    '#f4a0a0': (-100, 0),       # light salmon pink (negative values)
    '#f7b89a': (0, 1),          # peach
    '#faca8a': (1, 5),          # light apricot
    '#fad87a': (5, 20),         # pastel gold
    '#f8e87a': (20, 80),        # light yellow
    '#e8f0a0': (80, 250),       # pale lime
    '#c0ecb8': (250, 800),      # mint cream
    '#a8e0d0': (800, 2500),     # light aqua
    '#a0d0e8': (2500, 8000),    # pale sky
    '#f8f0e0': (8000, 25000),   # ivory             (highest values)
}

# Strong-contrast mapping used exclusively for the scatter plot.
# Four vivid colors with boundaries chosen near the quartiles of the
# quadrupole potential at default scatter resolution so that each
# color covers roughly 25 % of the data points.
SCATTER_COLOR_MAPPING = {
    'red':    (0, 8),
    'orange': (8, 150),
    'green':  (150, 1200),
    'blue':   (1200, 25000),
}


# =====================================================================
# Physics functions
# =====================================================================

def quadrupole_collective_potential(beta, gamma, spin):
    """
    Quadrupole collective potential V(beta, gamma, I).
    gamma is expected in degrees and converted internally to radians.
    """
    gamma = gamma * np.pi / 180  # radians
    c_beta, c_gamma, moi0 = 1, 1.5, 20.0
    beta_0 = 0.1
    def moi(_b, _g): return moi0 * np.power(_b, 2) * (1.0 + np.cos(3 * _g))
    t1 = 0.5 * c_beta * np.power(beta - beta_0, 2)
    t2 = 0.5 * c_gamma * np.power(gamma, 2)
    t3 = 0.5 * moi(beta, gamma) * spin * (spin + 1)
    return t1 + t2 + t3


def mexican_hat_potential(r, theta, lambda_=1.0, v=1.0, epsilon=0.3, n=3):
    r"""
    Mexican hat (sombrero) potential with angular perturbation:

        V(r, \theta) = \lambda (r^2 - v^2)^2
                     + \epsilon \, r^2 \cos(n \theta)

    The r^2 factor on the perturbation ensures V -> 0 smoothly
    at the origin.
    """
    return lambda_ * (r**2 - v**2)**2 + epsilon * r**2 * np.cos(n * theta)


def gaussian_3d(x, y, z):
    r"""
    Spherically symmetric 3D Gaussian:

        f(x, y, z) = e^{-(x^2 + y^2 + z^2)}

    Equivalently, f(r) = e^{-r^2} where r = \sqrt{x^2 + y^2 + z^2}.
    """
    return np.exp(-(x**2 + y**2 + z**2))


# =====================================================================
# Color utilities
# =====================================================================

def assign_colors(f_values, color_mapping):
    """
    Assign a color to each value in f_values based on the color_mapping
    dictionary.

    color_mapping format: {"color_name": (lower_bound, upper_bound), ...}

    For values outside all intervals, the nearest interval boundary
    is used (clamping).
    """
    sorted_entries = sorted(color_mapping.items(), key=lambda item: item[1][0])

    colors = []
    for val in f_values:
        assigned = None
        for color, (low, high) in sorted_entries:
            if low <= val < high:
                assigned = color
                break

        if assigned is None:
            if val < sorted_entries[0][1][0]:
                assigned = sorted_entries[0][0]
            else:
                assigned = sorted_entries[-1][0]

        colors.append(assigned)

    return colors


def colors_to_facecolors(F_2d, color_mapping):
    """
    Convert a 2D array of function values into an RGBA facecolors array
    suitable for plot_surface's ``facecolors`` parameter.

    plot_surface with an (M, N) meshgrid has (M-1) x (N-1) faces.
    For each face the function value is the average of its four corner
    vertices.

    Returns an (M-1, N-1, 4) RGBA array.
    """
    M, N = F_2d.shape
    F_faces = 0.25 * (F_2d[:-1, :-1] + F_2d[1:, :-1] +
                       F_2d[:-1, 1:] + F_2d[1:, 1:])

    face_colors_flat = assign_colors(F_faces.ravel(), color_mapping)

    rgba = np.array([mcolors.to_rgba(c) for c in face_colors_flat])
    return rgba.reshape(M - 1, N - 1, 4)


def build_legend(color_mapping, f_values):
    """
    Build legend handles from the color_mapping dictionary,
    including only intervals that contain at least one data point
    from *f_values*.  Also prints the actual data range.

    f_values : 1-D array (or flat array) of all function values
               present in the plot.
    """
    f_min, f_max = np.min(f_values), np.max(f_values)
    print(f"  Legend: showing intervals that overlap "
          f"[{f_min:.4f}, {f_max:.4f}]")

    sorted_entries = sorted(color_mapping.items(), key=lambda item: item[1][0])
    handles = []
    for color, (low, high) in sorted_entries:
        # Check if any data point falls in this interval (or is clamped to it)
        count = np.sum((f_values >= low) & (f_values < high))
        # Also include the lowest interval if data is below it (clamping)
        if count == 0 and low == sorted_entries[0][1][0] and np.any(f_values < low):
            count = 1
        # Also include the highest interval if data is above it (clamping)
        if count == 0 and high == sorted_entries[-1][1][1] and np.any(f_values >= high):
            count = 1
        if count > 0:
            label = f'$[{low:g},\\;{high:g})$'
            patch = mpatches.Patch(color=color, label=label)
            handles.append(patch)
    return handles


# =====================================================================
# Mode 1: Default — Fixed-spin surface slices (2x2 subplot grid)
# =====================================================================

def run_default(resolution=None, output=None):
    r"""
    Plot V(\beta, \gamma) as a surface for four fixed spin values
    in a 2x2 subplot grid.  Each surface is colored using the global
    COLOR_MAPPING based on the function value at each face.
    """
    _range = resolution or 20

    beta_vals = np.linspace(0, 0.6, _range)
    gamma_vals = np.linspace(-30, 90, _range)  # degrees

    B, G = np.meshgrid(beta_vals, gamma_vals, indexing='ij')

    spin_values = [2, 10, 20, 40]

    # Collect all face-level F values across subplots for the legend
    all_face_values = []

    fig = plt.figure(figsize=(14, 11))
    fig.suptitle(
        r'$V(\beta,\,\gamma,\,I) = \frac{1}{2}c_\beta(\beta - \beta_0)^2'
        r' + \frac{1}{2}c_\gamma\gamma^2'
        r' + \frac{1}{2}\mathcal{I}(\beta,\gamma)\,I(I+1)$',
    )

    for idx, spin in enumerate(spin_values, start=1):
        ax = fig.add_subplot(2, 2, idx, projection='3d')

        F = quadrupole_collective_potential(B, G, spin)

        print(f"  Spin I = {spin:5.1f}  ->  "
              f"V range: [{F.min():.4f}, {F.max():.4f}]")

        # Compute face values (same averaging as colors_to_facecolors)
        F_faces = 0.25 * (F[:-1, :-1] + F[1:, :-1] +
                          F[:-1, 1:] + F[1:, 1:])
        all_face_values.append(F_faces.ravel())

        facecolors = colors_to_facecolors(F, COLOR_MAPPING)

        ax.plot_surface(B, G, F,
                        facecolors=facecolors,
                        rstride=1, cstride=1,
                        linewidth=0.1, antialiased=True,
                        shade=False)

        ax.set_xlabel(r'$\beta$')
        ax.set_ylabel(r'$\gamma\;[\mathrm{deg}]$')
        ax.set_zlabel(r'$V\;[\mathrm{a.u.}]$')
        ax.set_title(r'$I = %g$' % spin)

    all_F = np.concatenate(all_face_values)
    legend_handles = build_legend(COLOR_MAPPING, all_F)
    fig.legend(handles=legend_handles, loc='lower center',
               ncol=len(legend_handles), frameon=True, fancybox=True)

    fig.subplots_adjust(left=0.02, right=0.98,
                        bottom=0.08, top=0.92,
                        wspace=0.15, hspace=0.18)
    if output:
        fig.savefig(output, bbox_inches='tight', dpi=150)
        print(f"  Saved: {output}")
    plt.show()


# =====================================================================
# Mode 2: Spherical — Mexican hat potential on a surface of revolution
# =====================================================================

def run_spherical(resolution=None, output=None):
    r"""
    Plot the Mexican hat potential V(r, \theta) as a 3D surface using
    cylindrical coordinate mapping:

        x = r \cos\theta ,\quad y = r \sin\theta ,\quad z = V(r, \theta)

    The surface is colored using the global COLOR_MAPPING based on the
    function value at each face.
    """
    # Mexican hat parameters
    lambda_ = 1.0
    v = 1.0
    epsilon = 0.8
    n = 3

    # Resolution (radial and angular derived from the single parameter)
    _base = resolution or 20
    n_r = _base * 2
    n_theta = _base * 3

    r_vals = np.linspace(0, 2.0, n_r)
    theta_vals = np.linspace(0, 2 * np.pi, n_theta)

    R, THETA = np.meshgrid(r_vals, theta_vals, indexing='ij')

    V = mexican_hat_potential(R, THETA, lambda_=lambda_, v=v,
                              epsilon=epsilon, n=n)

    print(f"  Mexican hat V(r, theta) range: "
          f"min = {V.min():.4f}, max = {V.max():.4f}")

    # Cylindrical -> Cartesian for plotting
    X = R * np.cos(THETA)
    Y = R * np.sin(THETA)
    Z = V

    facecolors = colors_to_facecolors(V, COLOR_MAPPING)

    # Face-level values for the legend filter
    V_faces = 0.25 * (V[:-1, :-1] + V[1:, :-1] +
                       V[:-1, 1:] + V[1:, 1:])

    # --- Plot ---
    fig = plt.figure(figsize=(11, 9))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X, Y, Z,
                    facecolors=facecolors,
                    rstride=1, cstride=1,
                    edgecolor='#40404060',
                    linewidth=0.3, antialiased=True,
                    shade=False)

    ax.set_xlabel(r'$r\cos\theta$')
    ax.set_ylabel(r'$r\sin\theta$')
    ax.set_zlabel(r'$V(r,\,\theta)$')
    ax.set_title(
        r'$V(r,\,\theta) = \lambda\,(r^2 - v^2)^2 '
        r'+ \varepsilon\, r^2 \cos(n\theta)$'
        '\n'
        r'$\lambda = %.1f,\quad v = %.1f,\quad '
        r'\varepsilon = %.2f,\quad n = %d$'
        % (lambda_, v, epsilon, n),
    )

    legend_handles = build_legend(COLOR_MAPPING, V_faces.ravel())
    ax.legend(handles=legend_handles, loc='upper left',
              title=r'$V(r,\theta)$ intervals')

    plt.tight_layout()
    if output:
        fig.savefig(output, bbox_inches='tight', dpi=150)
        print(f"  Saved: {output}")
    plt.show()


# =====================================================================
# Mode 3: Scatter — 3D scatter plot of V(beta, gamma, spin)
# =====================================================================

def run_scatter(resolution=None, output=None):
    r"""
    Plot the quadrupole collective potential as a 3D scatter plot.

    Each point (beta, gamma, spin) in the parameter space is shown as
    a marker whose color encodes the function value V(beta, gamma, spin)
    via the dedicated SCATTER_COLOR_MAPPING (strong, vivid colors).
    """
    _range = resolution or 10

    beta_vals = np.linspace(0, 0.6, _range)
    gamma_vals = np.linspace(-30, 90, _range)   # degrees
    spin_vals = np.linspace(0.5, 50.5, _range)

    B, G, S = np.meshgrid(beta_vals, gamma_vals, spin_vals, indexing='ij')

    b_flat = B.ravel()
    g_flat = G.ravel()
    s_flat = S.ravel()

    F = quadrupole_collective_potential(b_flat, g_flat, s_flat)

    print(f"  V(beta, gamma, spin) range: "
          f"min = {F.min():.4f}, max = {F.max():.4f}")

    colors = assign_colors(F, SCATTER_COLOR_MAPPING)

    # --- Plot ---
    fig = plt.figure(figsize=(11, 9))
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(b_flat, g_flat, s_flat,
               c=colors, s=14, alpha=0.8, edgecolors='none')

    ax.set_xlabel(r'$\beta$')
    ax.set_ylabel(r'$\gamma\;[\mathrm{deg}]$')
    ax.set_zlabel(r'$I$ (spin)')
    ax.set_title(
        r'$V(\beta,\,\gamma,\,I) = \frac{1}{2}c_\beta(\beta - \beta_0)^2'
        r' + \frac{1}{2}c_\gamma\gamma^2'
        r' + \frac{1}{2}\mathcal{I}(\beta,\gamma)\,I(I+1)$'
    )

    legend_handles = build_legend(SCATTER_COLOR_MAPPING, F)
    ax.legend(handles=legend_handles, loc='upper left',
              title=r'$V(\beta,\gamma,I)$ intervals')

    plt.tight_layout()
    if output:
        fig.savefig(output, bbox_inches='tight', dpi=150)
        print(f"  Saved: {output}")
    plt.show()


# =====================================================================
# Mode 4: Gaussian — 3D Gaussian scatter cloud with gray gradient
# =====================================================================

def run_gaussian(resolution=None, output=None):
    r"""
    Plot f(x,y,z) = e^{-(x^2+y^2+z^2)} as a spherical scatter cloud.

    Only points inside the sphere r <= r_max are plotted so the cloud
    has a spherical shape.  A continuous grayscale colormap (dark at the
    center, light at the edges) is used instead of discrete color bins.
    Per-point alpha makes the outer shell semi-transparent so the dense
    dark core is visible from outside.
    """
    _range = resolution or 40
    r_max = 2.0

    vals = np.linspace(-r_max, r_max, _range)
    X, Y, Z = np.meshgrid(vals, vals, vals, indexing='ij')

    x_flat = X.ravel()
    y_flat = Y.ravel()
    z_flat = Z.ravel()

    # Spherical filter: keep only points inside the sphere
    r = np.sqrt(x_flat**2 + y_flat**2 + z_flat**2)
    mask = r <= r_max

    x_s = x_flat[mask]
    y_s = y_flat[mask]
    z_s = z_flat[mask]

    F = gaussian_3d(x_s, y_s, z_s)

    print(f"  f(x,y,z) range: min = {F.min():.6f}, max = {F.max():.6f}")
    print(f"  Points plotted: {len(F)} / {len(x_flat)} "
          f"(spherical filter r <= {r_max})")

    # Per-point alpha: use a steep power law so the outer shell is
    # very transparent (letting you see the dark core) while the
    # center stays opaque.   f^5 drops off extremely fast:
    #   f=1.0 (center)  -> alpha = 1.0
    #   f=0.78 (r=0.5)  -> alpha = 0.31
    #   f=0.37 (r=1.0)  -> alpha = 0.02
    #   f=0.11 (r=1.5)  -> alpha = 0.02
    alpha_min = 0.02
    alphas = alpha_min + (1.0 - alpha_min) * F**5

    # Build RGBA array using the 'copper' colormap.
    # copper: black (high f, center) -> warm bronze/tan (low f, edges).
    # All tones are clearly visible — no white that vanishes into the
    # background.  The colormap is reversed so that the dense core is
    # the darkest.
    cmap = plt.get_cmap('copper_r')
    norm = mcolors.Normalize(vmin=0.0, vmax=1.0)
    rgba = cmap(norm(F))       # (N, 4) array with default alpha = 1
    rgba[:, 3] = alphas        # override alpha channel

    # Scale marker size inversely with resolution so that at higher
    # density the points overlap and form a continuous-looking sphere.
    marker_size = max(1, int(800 / _range))

    # --- Plot ---
    fig = plt.figure(figsize=(10, 9))
    ax = fig.add_subplot(111, projection='3d')

    sc = ax.scatter(x_s, y_s, z_s,
                    c=F, cmap='copper_r',
                    vmin=0.0, vmax=1.0,
                    s=marker_size, edgecolors='none')

    # Overwrite the rendered colors with our per-point alpha version
    sc.set_facecolors(rgba)

    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.set_zlabel(r'$z$')
    ax.set_title(r'$f(x,\,y,\,z) = e^{-(x^2 + y^2 + z^2)}$')

    # Equal aspect ratio so the sphere isn't squashed
    ax.set_box_aspect([1, 1, 1])

    # Colorbar showing the grayscale mapping
    cbar = fig.colorbar(sc, ax=ax, shrink=0.6, pad=0.08)
    cbar.set_label(r'$f(x,y,z)$')

    plt.tight_layout()
    if output:
        fig.savefig(output, bbox_inches='tight', dpi=150)
        print(f"  Saved: {output}")
    plt.show()


# =====================================================================
# Entry point
# =====================================================================

def main():
    parser = argparse.ArgumentParser(
        description='3D Color Plot: visualize physics potentials with '
                    'custom color mappings.'
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        '--spherical', action='store_true',
        help='Spherical coordinate representation with the '
             'Mexican hat potential.'
    )
    mode.add_argument(
        '--scatter', action='store_true',
        help='3D scatter plot of V(beta, gamma, spin) where each '
             'point is colored by the function value.'
    )
    mode.add_argument(
        '--gaussian', action='store_true',
        help='3D Gaussian scatter cloud f(x,y,z) = exp(-(x^2+y^2+z^2)) '
             'with a continuous grayscale gradient.'
    )
    parser.add_argument(
        '-n', '--resolution', type=int, default=None,
        help='Number of grid points per axis.  Lower values give '
             'faster interactive rotation; higher values give finer '
             'detail.  Defaults: 20 (default/spherical), 10 (scatter).'
    )
    parser.add_argument(
        '-o', '--output', type=str, default=None,
        help='Save the figure to this file path (e.g. example.pdf). '
             'The format is inferred from the extension.'
    )
    args = parser.parse_args()

    n = args.resolution
    o = args.output

    if args.spherical:
        run_spherical(n, o)
    elif args.scatter:
        run_scatter(n, o)
    elif args.gaussian:
        run_gaussian(n, o)
    else:
        run_default(n, o)


if __name__ == "__main__":
    main()
