"""
Cutaway sphere visualization of f(x,y,z) = exp(-(x^2 + y^2 + z^2)).

One octant (x>0, y>0, z>0) is removed to expose three cross-sectional
faces and the internal radial gradient.

Usage:
    python cutaway_sphere.py                  # gray colormap (default)
    python cutaway_sphere.py --copper         # copper colormap
    python cutaway_sphere.py --copper -o out.pdf
"""
import argparse

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np

# =====================================================================
# Configuration
# =====================================================================
R_MAX = 1.1                         # sphere radius
LIMIT = R_MAX+0.3
F_RMAX = 0.2981972794
F_MIN = 0.2          # colormap / colorbar lower bound
F_MAX = 1.1                         # colormap / colorbar upper bound
N_TILES = 10                        # tiles per direction
PTS_PER_TILE = 3                    # mesh points per tile edge
EDGE_COLOR = "#f0f0f0ff"            # white with 38% opacity
EDGE_COLOR = "#50505040"            # white with 38% opacity
EDGE_WIDTH = 0.2                  # mesh grid line width
# Colormap presets — pure [0, 1] mapping, no shifting.
COLORMAP_PRESETS = {
    'gray':    'gray_r',            # black (center) -> white (surface)
    'copper':  'copper_r',          # black (center) -> copper (surface)
    'thermal': 'RdYlBu_r',         # red (center) -> blue (surface)
}

# alternative: https://cn.comsol.com/support/learning-center/course/modeling-with-partial-differential-equations-in-comsol-multiphysics-142/modeling-with-pdes-poissons-and-laplace-equations-43131

# Academic font styling
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Computer Modern Roman', 'CMU Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'cm',
    'axes.labelsize': 13,
    'axes.titlesize': 14,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.titlesize': 15,
})


# =====================================================================
# Physics function
# =====================================================================

def gaussian_3d(x, y, z):
    return np.exp(-(x**2 + y**2 + z**2))


# =====================================================================
# Helpers
# =====================================================================

def facecolors_from_F(F_2d, cmap_name, vmin, vmax):
    """Map a 2D function-value array to an (M-1, N-1, 4) RGBA facecolor array."""
    M, N = F_2d.shape
    F_faces = 0.25 * (F_2d[:-1, :-1] + F_2d[1:, :-1] +
                      F_2d[:-1, 1:] + F_2d[1:, 1:])
    cmap = plt.get_cmap(cmap_name)
    norm = mcolors.Normalize(vmin=vmin, vmax=vmax)
    return cmap(norm(F_faces))


def _plot_tile(ax, X, Y, Z, fc, lw):
    """Render a single small surface tile."""
    ax.plot_surface(X, Y, Z, facecolors=fc,
                    rstride=1, cstride=1, shade=False,
                    edgecolor=EDGE_COLOR, linewidth=lw)


# =====================================================================
# Surface builders
# =====================================================================

def build_outer_shell(ax, r, n_tiles, cmap_name, vmin, vmax):
    """Render the 3/4 outer shell as a grid of small tiles."""
    f_surface = np.exp(-r**2)
    p = PTS_PER_TILE
    lw = EDGE_WIDTH / 2

    # Bottom hemisphere (theta: pi/2 -> pi, phi: 0 -> 2*pi)
    th_edges = np.linspace(np.pi / 2, np.pi, n_tiles + 1)
    ph_edges = np.linspace(0, 2 * np.pi, 2 * n_tiles + 1)

    for i in range(n_tiles):
        for j in range(2 * n_tiles):
            th = np.linspace(th_edges[i], th_edges[i + 1], p)
            ph = np.linspace(ph_edges[j], ph_edges[j + 1], p)
            TH, PH = np.meshgrid(th, ph, indexing='ij')
            X = r * np.sin(TH) * np.cos(PH)
            Y = r * np.sin(TH) * np.sin(PH)
            Z = r * np.cos(TH)
            F = np.full_like(X, f_surface)
            _plot_tile(ax, X, Y, Z,
                       facecolors_from_F(F, cmap_name, vmin, vmax), lw)

    # Top 3/4 hemisphere (theta: 0 -> pi/2, phi: pi/2 -> 2*pi)
    th_edges_t = np.linspace(0, np.pi / 2, n_tiles + 1)
    ph_edges_t = np.linspace(np.pi / 2, 2 * np.pi, int(1.5 * n_tiles) + 1)
    n_ph_t = len(ph_edges_t) - 1

    for i in range(n_tiles):
        for j in range(n_ph_t):
            th = np.linspace(th_edges_t[i], th_edges_t[i + 1], p)
            ph = np.linspace(ph_edges_t[j], ph_edges_t[j + 1], p)
            TH, PH = np.meshgrid(th, ph, indexing='ij')
            X = r * np.sin(TH) * np.cos(PH)
            Y = r * np.sin(TH) * np.sin(PH)
            Z = r * np.cos(TH)
            F = np.full_like(X, f_surface)
            _plot_tile(ax, X, Y, Z,
                       facecolors_from_F(F, cmap_name, vmin, vmax), lw)


def build_cut_face(ax, plane, r_max, n_tiles, cmap_name, vmin, vmax):
    """Build one cross-sectional quarter-disk as a 2D grid of small tiles."""
    r_edges = np.linspace(0, r_max, n_tiles + 1)
    ang_edges = np.linspace(0, np.pi / 2, n_tiles + 1)
    p = PTS_PER_TILE

    for i in range(n_tiles):
        for j in range(n_tiles):
            rv = np.linspace(r_edges[i], r_edges[i + 1], p)
            av = np.linspace(ang_edges[j], ang_edges[j + 1], p)
            R, ANG = np.meshgrid(rv, av, indexing='ij')

            if plane == 'xz':
                X, Y, Z = R * np.cos(ANG), np.zeros_like(R), R * np.sin(ANG)
            elif plane == 'yz':
                X, Y, Z = np.zeros_like(R), R * np.cos(ANG), R * np.sin(ANG)
            else:
                X, Y, Z = R * np.cos(ANG), R * np.sin(ANG), np.zeros_like(R)

            F = gaussian_3d(X, Y, Z)
            fc = facecolors_from_F(F, cmap_name, vmin, vmax)

            _plot_tile(ax, X, Y, Z, fc, EDGE_WIDTH)
            _plot_tile(ax, X[::-1], Y[::-1], Z[::-1], fc[::-1], EDGE_WIDTH)


# =====================================================================
# Main
# =====================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Cutaway sphere of f(x,y,z) = exp(-(x²+y²+z²)).')
    parser.add_argument('-o', '--output', type=str, default=None,
                        help='Save figure to this path (e.g. cutaway.pdf).')
    cmap_group = parser.add_mutually_exclusive_group()
    cmap_group.add_argument('--copper', action='store_true',
                            help='Use copper colormap (warm tones).')
    cmap_group.add_argument('--thermal', action='store_true',
                            help='Use thermal colormap (red=hot center, '
                                 'blue=cold surface).')
    args = parser.parse_args()

    # Select colormap preset
    if args.copper:
        preset = 'copper'
    elif args.thermal:
        preset = 'thermal'
    else:
        preset = 'gray'
    cmap_name = COLORMAP_PRESETS[preset]

    fig = plt.figure(figsize=(10, 9))
    ax = fig.add_subplot(111, projection='3d')

    # Outer shell (3/4 sphere, tiled)
    build_outer_shell(ax, R_MAX, N_TILES, cmap_name, F_MIN, F_MAX)

    # Three exposed cross-section faces (double-sided, tiled)
    for plane in ('xz', 'yz', 'xy'):
        build_cut_face(ax, plane, R_MAX, N_TILES, cmap_name, F_MIN, F_MAX)

    # Labels and title
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.set_zlabel(r'$z$')
    ax.set_title(r'$f(x,\,y,\,z) = e^{-(x^2 + y^2 + z^2)}$')
    ax.set_xlim(-LIMIT, LIMIT)
    ax.set_ylim(-LIMIT, LIMIT)
    ax.set_zlim(-LIMIT, LIMIT)
    ax.set_box_aspect([1, 1, 1])

    # Colorbar: straight [0, 1] range, no truncation or shifting
    full_cmap = plt.get_cmap(cmap_name)
    # Map CBAR_MIN and CBAR_MAX through the same norm used by surfaces
    norm_surf = mcolors.Normalize(vmin=F_MIN, vmax=F_MAX)
    CBAR_MIN = 0.2
    CBAR_MAX = 1
    cmap_lo = float(norm_surf(CBAR_MIN))   # where CBAR_MIN sits on [0,1]
    cmap_hi = float(norm_surf(CBAR_MAX))   # where CBAR_MAX sits on [0,1]
    trunc_cmap = mcolors.LinearSegmentedColormap.from_list(
        f'{cmap_name}_trunc',
        full_cmap(np.linspace(cmap_lo, cmap_hi, 256))
    )
    sm = plt.cm.ScalarMappable(
        cmap=trunc_cmap,
        norm=mcolors.Normalize(vmin=CBAR_MIN, vmax=CBAR_MAX))
    # sm = plt.cm.ScalarMappable(
    #     cmap=cmap_name)
    cbar = fig.colorbar(sm, ax=ax, shrink=0.6, pad=0.08)
    cbar.set_label(r'$f(x,y,z)$')

    # ax.view_init(elev=28, azim=50)
    ax.view_init(elev=29, azim=43)

    plt.tight_layout()
    if args.output:
        fig.savefig(args.output, bbox_inches='tight', dpi=300)
        print(f"  Saved: {args.output}")
    plt.show()


if __name__ == '__main__':
    main()
