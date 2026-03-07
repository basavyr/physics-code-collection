import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


def quadrupole_collective_potential(beta, gamma, spin):
    gamma = gamma * np.pi / 180  # radians
    c_beta, c_gamma, moi0 = 1, 1.5, 20.0
    beta_0 = 0.1
    def moi(_b, _g): return moi0 * np.power(_b, 2) * (1.0 + np.cos(3 * _g))
    t1 = 0.5 * c_beta * np.power(beta - beta_0, 2)
    t2 = 0.5 * c_gamma * np.power(gamma, 2)
    t3 = 0.5 * moi(beta, gamma) * spin * (spin + 1)
    return t1 + t2 + t3


def assign_colors(f_values, color_mapping):
    """
    Assign a color to each value in f_values based on the color_mapping dictionary.

    color_mapping format: {"color_name": (lower_bound, upper_bound), ...}

    For values outside all intervals, the nearest interval boundary is used
    (i.e., the lowest interval catches everything below it, 
     the highest interval catches everything above it).
    """
    # Sort intervals by their lower bound to determine ordering
    sorted_entries = sorted(color_mapping.items(), key=lambda item: item[1][0])

    colors = []
    for val in f_values:
        assigned = None
        for color, (low, high) in sorted_entries:
            if low <= val < high:
                assigned = color
                break

        if assigned is None:
            # Clamp to nearest interval
            if val < sorted_entries[0][1][0]:
                # Below the lowest interval -> use the lowest interval's color
                assigned = sorted_entries[0][0]
            else:
                # Above the highest interval -> use the highest interval's color
                assigned = sorted_entries[-1][0]

        colors.append(assigned)

    return colors


def main():
    # ----------------------------------------------------------------
    # Color mapping: each key is a color, each value is an (low, high)
    # interval for the function value F(beta, gamma, spin).
    #
    # PLACEHOLDER intervals: run the script once to see the printed
    # min/max of F, then adjust these intervals to meaningful ranges.
    # ----------------------------------------------------------------
    color_mapping = {
        "red": (0, 500),
        "green": (501, 5000),
        "blue": (5001, 20000),
    }

    # Grid resolution per axis (~20 gives 8000 points, fast to render)
    _range = 8

    # Realistic parameter ranges
    beta_vals = np.linspace(0, 0.6, _range)        # deformation parameter
    gamma_vals = np.linspace(-30, 90, _range)       # gamma in degrees
    spin_vals = np.linspace(0.5, 50.5, _range)      # nuclear spin

    # Create full 3D meshgrid (all combinations of beta, gamma, spin)
    B, G, S = np.meshgrid(beta_vals, gamma_vals, spin_vals, indexing='ij')

    # Flatten for vectorized computation and scatter plotting
    b_flat = B.ravel()
    g_flat = G.ravel()
    s_flat = S.ravel()

    # Compute function values
    F = quadrupole_collective_potential(b_flat, g_flat, s_flat)

    # Print the range so the user can define meaningful color_mapping intervals
    print(
        f"F(beta, gamma, spin) range: min = {F.min():.4f}, max = {F.max():.4f}")

    # Assign colors based on the color_mapping intervals
    colors = assign_colors(F, color_mapping)

    # --- 3D Scatter Plot ---
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(b_flat, g_flat, s_flat, c=colors,
               s=8, alpha=0.6, edgecolors='none')

    ax.set_xlabel(r'$\beta$ (deformation)')
    ax.set_ylabel(r'$\gamma$ (degrees)')
    ax.set_zlabel(r'$I$ (spin)')
    ax.set_title(r'Quadrupole Collective Potential $V(\beta, \gamma, I)$')

    # Build a legend from the color_mapping
    legend_handles = []
    for color, (low, high) in color_mapping.items():
        patch = mpatches.Patch(color=color, label=f'{color}: [{low}, {high})')
        legend_handles.append(patch)
    ax.legend(handles=legend_handles, loc='upper left', fontsize=9)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
