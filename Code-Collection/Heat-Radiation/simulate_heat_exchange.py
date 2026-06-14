from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt


SIGMA = 5.670374419e-8
RHO_WATER = 1000.0
CP_WATER = 4184.0
T_AMBIENT = 298.15
T_SURROUNDINGS = 298.15
H_CONV = 7.0
DT = 10.0
T_END = 4.0 * 3600.0
ROOM_TOLERANCE = 0.5


@dataclass(frozen=True)
class Body:
    name: str
    initial_temperature_k: float
    volume_m3: float
    area_m2: float
    emissivity: float

    @property
    def mass_kg(self) -> float:
        return RHO_WATER * self.volume_m3

    @property
    def heat_capacity_j_per_k(self) -> float:
        return self.mass_kg * CP_WATER


def heat_input_w(body: Body, temperature_k: float) -> tuple[float, float, float]:
    q_conv = body.area_m2 * H_CONV * (T_AMBIENT - temperature_k)
    q_rad = body.emissivity * SIGMA * body.area_m2 * (
        T_SURROUNDINGS**4 - temperature_k**4
    )
    return q_conv, q_rad, q_conv + q_rad


def simulate(body: Body) -> list[dict[str, float]]:
    temperature = body.initial_temperature_k
    rows: list[dict[str, float]] = []
    steps = int(T_END / DT)

    for step in range(steps + 1):
        time_s = step * DT
        q_conv, q_rad, q_total = heat_input_w(body, temperature)
        rows.append(
            {
                "time_s": time_s,
                "time_min": time_s / 60.0,
                "temperature_k": temperature,
                "temperature_c": temperature - 273.15,
                "q_conv_w": q_conv,
                "q_rad_w": q_rad,
                "q_total_w": q_total,
            }
        )
        temperature += (DT / body.heat_capacity_j_per_k) * q_total

    return rows


def first_time_within_ambient(rows: list[dict[str, float]]) -> float | None:
    for row in rows:
        if abs(row["temperature_k"] - T_AMBIENT) <= ROOM_TOLERANCE:
            return row["time_min"]
    return None


def sample_at_minutes(rows: list[dict[str, float]], minutes: list[float]) -> list[dict[str, float]]:
    sampled = []
    for minute in minutes:
        row = min(rows, key=lambda r: abs(r["time_min"] - minute))
        sampled.append(row)
    return sampled


def write_csv(path: Path, body: Body, rows: list[dict[str, float]]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "body",
                "time_min",
                "temperature_c",
                "q_conv_w",
                "q_rad_w",
                "q_total_w",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "body": body.name,
                    "time_min": f"{row['time_min']:.6g}",
                    "temperature_c": f"{row['temperature_c']:.6g}",
                    "q_conv_w": f"{row['q_conv_w']:.6g}",
                    "q_rad_w": f"{row['q_rad_w']:.6g}",
                    "q_total_w": f"{row['q_total_w']:.6g}",
                }
            )


def write_summary(path: Path, summaries: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "body",
                "initial_c",
                "direction",
                "time_to_within_0p5c_min",
                "temperature_10_min_c",
                "temperature_15_min_c",
                "temperature_30_min_c",
                "temperature_60_min_c",
                "temperature_120_min_c",
            ],
        )
        writer.writeheader()
        writer.writerows(summaries)


def plot_results(
    path: Path,
    water_rows: list[dict[str, float]],
    coffee_rows: list[dict[str, float]],
    water_threshold_min: float | None,
    coffee_threshold_min: float | None,
) -> None:
    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.size": 11,
            "axes.labelsize": 12,
            "axes.titlesize": 13,
            "legend.fontsize": 10,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "figure.dpi": 150,
            "savefig.dpi": 300,
        }
    )

    fig, ax = plt.subplots(figsize=(7.2, 4.6), constrained_layout=True)
    marker_minutes = list(range(0, int(T_END / 60) + 1, 10))
    water_marker_rows = sample_at_minutes(water_rows, marker_minutes)
    coffee_marker_rows = sample_at_minutes(coffee_rows, marker_minutes)
    ax.plot(
        [row["time_min"] for row in water_rows],
        [row["temperature_c"] for row in water_rows],
        color="#1f77b4",
        linewidth=2.3,
        label="Cold water glass",
    )
    ax.plot(
        [row["time_min"] for row in water_marker_rows],
        [row["temperature_c"] for row in water_marker_rows],
        color="#1f77b4",
        marker="o",
        linestyle="none",
        markersize=3.3,
        alpha=0.75,
    )
    ax.plot(
        [row["time_min"] for row in coffee_rows],
        [row["temperature_c"] for row in coffee_rows],
        color="#8c2d04",
        linewidth=2.3,
        label="Hot espresso cup",
    )
    ax.plot(
        [row["time_min"] for row in coffee_marker_rows],
        [row["temperature_c"] for row in coffee_marker_rows],
        color="#8c2d04",
        marker="s",
        linestyle="none",
        markersize=3.3,
        alpha=0.75,
    )
    ax.axhline(
        T_AMBIENT - 273.15,
        color="black",
        linestyle="--",
        linewidth=1.4,
        label="Room temperature",
    )
    ax.fill_between(
        [0, T_END / 60.0],
        T_AMBIENT - 273.15 - ROOM_TOLERANCE,
        T_AMBIENT - 273.15 + ROOM_TOLERANCE,
        color="black",
        alpha=0.07,
        linewidth=0,
        label=r"ambient $\pm 0.5^{\circ}$C band",
    )

    if water_threshold_min is not None:
        ax.axvline(water_threshold_min, color="#1f77b4", linestyle=":", linewidth=1.4)
        ax.annotate(
            f"water within 0.5°C\n{water_threshold_min:.0f} min",
            xy=(water_threshold_min, T_AMBIENT - 273.15),
            xytext=(water_threshold_min + 14, 11.0),
            arrowprops={"arrowstyle": "->", "color": "#1f77b4", "lw": 1.0},
            color="#1f77b4",
        )
    if coffee_threshold_min is not None:
        ax.axvline(coffee_threshold_min, color="#8c2d04", linestyle=":", linewidth=1.4)
        ax.annotate(
            f"coffee within 0.5°C\n{coffee_threshold_min:.0f} min",
            xy=(coffee_threshold_min, T_AMBIENT - 273.15),
            xytext=(coffee_threshold_min - 108, 48.0),
            arrowprops={"arrowstyle": "->", "color": "#8c2d04", "lw": 1.0},
            color="#8c2d04",
        )

    ax.set_title("Transient approach to room temperature")
    ax.set_xlabel("Time (min)")
    ax.set_ylabel("Temperature (°C)")
    ax.set_xlim(0, T_END / 60.0)
    ax.set_ylim(0, 72)
    ax.set_xticks(range(0, int(T_END / 60) + 1, 30))
    ax.grid(True, which="major", color="#d9d9d9", linewidth=0.8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(frameon=True, framealpha=0.94, loc="upper right")
    fig.savefig(path)
    plt.close(fig)


def main() -> None:
    base = Path(__file__).resolve().parent
    output_dir = base / "outputs"
    output_dir.mkdir(exist_ok=True)

    water = Body(
        name="Cold water glass",
        initial_temperature_k=277.15,
        volume_m3=2.80e-4,
        area_m2=0.032,
        emissivity=0.93,
    )
    coffee = Body(
        name="Hot espresso cup",
        initial_temperature_k=338.15,
        volume_m3=9.00e-5,
        area_m2=0.018,
        emissivity=0.92,
    )

    water_rows = simulate(water)
    coffee_rows = simulate(coffee)
    water_threshold = first_time_within_ambient(water_rows)
    coffee_threshold = first_time_within_ambient(coffee_rows)

    write_csv(output_dir / "water_temperature_evolution.csv", water, water_rows)
    write_csv(output_dir / "coffee_temperature_evolution.csv", coffee, coffee_rows)

    sample_minutes = [0, 10, 15, 30, 60, 120, 240]
    summaries = []
    for body, rows, threshold, direction in [
        (water, water_rows, water_threshold, "absorbs heat inward"),
        (coffee, coffee_rows, coffee_threshold, "loses heat outward"),
    ]:
        samples = sample_at_minutes(rows, sample_minutes)
        samples_by_min = {int(round(row["time_min"])): row for row in samples}
        summaries.append(
            {
                "body": body.name,
                "initial_c": f"{body.initial_temperature_k - 273.15:.2f}",
                "direction": direction,
                "time_to_within_0p5c_min": "not reached"
                if threshold is None
                else f"{threshold:.1f}",
                "temperature_10_min_c": f"{samples_by_min[10]['temperature_c']:.2f}",
                "temperature_15_min_c": f"{samples_by_min[15]['temperature_c']:.2f}",
                "temperature_30_min_c": f"{samples_by_min[30]['temperature_c']:.2f}",
                "temperature_60_min_c": f"{samples_by_min[60]['temperature_c']:.2f}",
                "temperature_120_min_c": f"{samples_by_min[120]['temperature_c']:.2f}",
            }
        )
    write_summary(output_dir / "temperature_summary.csv", summaries)
    plot_results(
        output_dir / "temperature_evolution.pdf",
        water_rows,
        coffee_rows,
        water_threshold,
        coffee_threshold,
    )
    plot_results(
        output_dir / "temperature_evolution.png",
        water_rows,
        coffee_rows,
        water_threshold,
        coffee_threshold,
    )

    for summary in summaries:
        print(summary)


if __name__ == "__main__":
    main()
