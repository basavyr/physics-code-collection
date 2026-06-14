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
K_AIR = 0.026
DT = 10.0
T_END = 4.0 * 3600.0
ROOM_TOLERANCE = 0.5
REFERENCE_GAP_M = 0.01
VIEW_FACTOR_AT_REFERENCE_GAP = 0.55
DISTANCES_CM = [1, 5, 10, 15, 20, 30]


@dataclass(frozen=True)
class Body:
    name: str
    initial_temperature_k: float
    volume_m3: float
    area_m2: float
    emissivity: float

    @property
    def heat_capacity_j_per_k(self) -> float:
        return RHO_WATER * self.volume_m3 * CP_WATER


def room_heat_input(body: Body, temperature_k: float) -> float:
    q_conv = body.area_m2 * H_CONV * (T_AMBIENT - temperature_k)
    q_rad = body.emissivity * SIGMA * body.area_m2 * (
        T_SURROUNDINGS**4 - temperature_k**4
    )
    return q_conv + q_rad


def pair_radiation_to_first(
    first_temperature_k: float,
    second_temperature_k: float,
    first_emissivity: float,
    second_emissivity: float,
    facing_area_m2: float,
    view_factor: float,
) -> float:
    effective_emissivity = 1.0 / (
        (1.0 / first_emissivity) + (1.0 / second_emissivity) - 1.0
    )
    return (
        effective_emissivity
        * SIGMA
        * facing_area_m2
        * view_factor
        * (second_temperature_k**4 - first_temperature_k**4)
    )


def pair_air_conduction_to_first(
    first_temperature_k: float,
    second_temperature_k: float,
    facing_area_m2: float,
    gap_m: float,
) -> float:
    return K_AIR * facing_area_m2 / gap_m * (second_temperature_k - first_temperature_k)


def view_factor_for_gap(gap_m: float) -> float:
    return min(
        0.95,
        VIEW_FACTOR_AT_REFERENCE_GAP * (REFERENCE_GAP_M / gap_m) ** 2,
    )


def simulate_alone(body: Body) -> list[dict[str, float]]:
    temperature = body.initial_temperature_k
    rows = []
    for step in range(int(T_END / DT) + 1):
        time_s = step * DT
        q_room = room_heat_input(body, temperature)
        rows.append(
            {
                "time_min": time_s / 60.0,
                "temperature_c": temperature - 273.15,
                "q_room_w": q_room,
                "q_pair_w": 0.0,
            }
        )
        temperature += DT * q_room / body.heat_capacity_j_per_k
    return rows


def simulate_coupled(
    coffee: Body,
    water: Body,
    facing_area_m2: float,
    gap_m: float,
    view_factor: float,
) -> tuple[list[dict[str, float]], list[dict[str, float]]]:
    coffee_temperature = coffee.initial_temperature_k
    water_temperature = water.initial_temperature_k
    coffee_rows = []
    water_rows = []

    for step in range(int(T_END / DT) + 1):
        time_s = step * DT
        q_coffee_room = room_heat_input(coffee, coffee_temperature)
        q_water_room = room_heat_input(water, water_temperature)
        q_pair_rad_to_coffee = pair_radiation_to_first(
            coffee_temperature,
            water_temperature,
            coffee.emissivity,
            water.emissivity,
            facing_area_m2,
            view_factor,
        )
        q_pair_air_to_coffee = pair_air_conduction_to_first(
            coffee_temperature,
            water_temperature,
            facing_area_m2,
            gap_m,
        )
        q_pair_to_coffee = q_pair_rad_to_coffee + q_pair_air_to_coffee
        q_pair_to_water = -q_pair_to_coffee

        coffee_rows.append(
            {
                "time_min": time_s / 60.0,
                "temperature_c": coffee_temperature - 273.15,
                "q_room_w": q_coffee_room,
                "q_pair_w": q_pair_to_coffee,
            }
        )
        water_rows.append(
            {
                "time_min": time_s / 60.0,
                "temperature_c": water_temperature - 273.15,
                "q_room_w": q_water_room,
                "q_pair_w": q_pair_to_water,
            }
        )

        coffee_temperature += DT * (q_coffee_room + q_pair_to_coffee) / coffee.heat_capacity_j_per_k
        water_temperature += DT * (q_water_room + q_pair_to_water) / water.heat_capacity_j_per_k

    return coffee_rows, water_rows


def first_time_within_ambient(rows: list[dict[str, float]]) -> float | None:
    for row in rows:
        if abs(row["temperature_c"] - (T_AMBIENT - 273.15)) <= ROOM_TOLERANCE:
            return row["time_min"]
    return None


def sample_at_minutes(rows: list[dict[str, float]], minutes: list[float]) -> dict[int, dict[str, float]]:
    return {
        int(minute): min(rows, key=lambda row: abs(row["time_min"] - minute))
        for minute in minutes
    }


def write_rows(path: Path, rows: list[dict[str, float]], label: str) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["body", "time_min", "temperature_c", "q_room_w", "q_pair_w"],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "body": label,
                    "time_min": f"{row['time_min']:.6g}",
                    "temperature_c": f"{row['temperature_c']:.6g}",
                    "q_room_w": f"{row['q_room_w']:.6g}",
                    "q_pair_w": f"{row['q_pair_w']:.6g}",
                }
            )


def write_summary(path: Path, summaries: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summaries[0].keys()))
        writer.writeheader()
        writer.writerows(summaries)


def plot_results(
    path: Path,
    coffee_alone: list[dict[str, float]],
    coffee_by_distance: dict[int, list[dict[str, float]]],
    coffee_alone_threshold: float | None,
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
    fig, ax = plt.subplots(figsize=(7.4, 4.7), constrained_layout=True)
    ax.plot(
        [row["time_min"] for row in coffee_alone],
        [row["temperature_c"] for row in coffee_alone],
        color="#8c2d04",
        linestyle="--",
        linewidth=2.4,
        label="Coffee alone",
    )
    colors = plt.cm.viridis_r([0.05, 0.22, 0.39, 0.56, 0.73, 0.90])
    for color, distance_cm in zip(colors, DISTANCES_CM):
        rows = coffee_by_distance[distance_cm]
        ax.plot(
            [row["time_min"] for row in rows],
            [row["temperature_c"] for row in rows],
            color=color,
            linewidth=2.0,
            label=f"Coffee + water, d = {distance_cm} cm",
        )
    ax.axhline(
        T_AMBIENT - 273.15,
        color="black",
        linestyle=":",
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
    )

    if coffee_alone_threshold is not None:
        ax.axvline(coffee_alone_threshold, color="#8c2d04", linestyle="--", linewidth=1.1, alpha=0.7)
    one_cm_rows = coffee_by_distance[1]
    one_cm_threshold = first_time_within_ambient(one_cm_rows)
    if one_cm_threshold is not None:
        ax.axvline(one_cm_threshold, color="#440154", linestyle=":", linewidth=1.4)
        ax.annotate(
            f"1 cm case within 0.5°C\n{one_cm_threshold:.0f} min",
            xy=(one_cm_threshold, T_AMBIENT - 273.15),
            xytext=(one_cm_threshold + 10, 43),
            arrowprops={"arrowstyle": "->", "color": "#440154", "lw": 1.0},
            color="#440154",
        )

    ax.set_title("Distance dependence of cold-water influence on espresso cooling")
    ax.set_xlabel("Time (min)")
    ax.set_ylabel("Temperature (°C)")
    ax.set_xlim(0, T_END / 60.0)
    ax.set_ylim(0, 72)
    ax.set_xticks(range(0, int(T_END / 60) + 1, 30))
    ax.grid(True, color="#d9d9d9", linewidth=0.8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(frameon=True, framealpha=0.95, loc="upper right", ncol=1)
    fig.savefig(path)
    plt.close(fig)


def main() -> None:
    base = Path(__file__).resolve().parent
    output_dir = base / "outputs"
    output_dir.mkdir(exist_ok=True)

    water = Body("Cold water glass", 277.15, 2.80e-4, 0.032, 0.93)
    coffee = Body("Hot espresso cup", 338.15, 9.00e-5, 0.018, 0.92)
    facing_area_m2 = 0.006

    coffee_alone = simulate_alone(coffee)
    coffee_by_distance: dict[int, list[dict[str, float]]] = {}
    water_by_distance: dict[int, list[dict[str, float]]] = {}

    coffee_alone_threshold = first_time_within_ambient(coffee_alone)
    for distance_cm in DISTANCES_CM:
        gap_m = distance_cm / 100.0
        coffee_rows, water_rows = simulate_coupled(
            coffee, water, facing_area_m2, gap_m, view_factor_for_gap(gap_m)
        )
        coffee_by_distance[distance_cm] = coffee_rows
        water_by_distance[distance_cm] = water_rows
        write_rows(
            output_dir / f"coupled_coffee_near_water_{distance_cm:02d}cm.csv",
            coffee_rows,
            f"Coffee near cold water, d={distance_cm} cm",
        )
        write_rows(
            output_dir / f"coupled_water_near_coffee_{distance_cm:02d}cm.csv",
            water_rows,
            f"Cold water near coffee, d={distance_cm} cm",
        )

    write_rows(output_dir / "coupled_coffee_alone.csv", coffee_alone, "Coffee alone")

    sample_minutes = [0, 10, 15, 30, 60, 120]
    alone_samples = sample_at_minutes(coffee_alone, sample_minutes)
    summaries = [
        {
            "distance_cm": "alone",
            "time_to_within_0p5c_min": f"{coffee_alone_threshold:.1f}",
            "temperature_10_min_c": f"{alone_samples[10]['temperature_c']:.2f}",
            "temperature_30_min_c": f"{alone_samples[30]['temperature_c']:.2f}",
            "temperature_60_min_c": f"{alone_samples[60]['temperature_c']:.2f}",
            "temperature_120_min_c": f"{alone_samples[120]['temperature_c']:.2f}",
            "initial_pair_heat_into_coffee_w": "0.000",
        },
    ]
    for distance_cm in DISTANCES_CM:
        rows = coffee_by_distance[distance_cm]
        samples = sample_at_minutes(rows, sample_minutes)
        threshold = first_time_within_ambient(rows)
        summaries.append(
            {
                "distance_cm": str(distance_cm),
                "time_to_within_0p5c_min": f"{threshold:.1f}",
                "temperature_10_min_c": f"{samples[10]['temperature_c']:.2f}",
                "temperature_30_min_c": f"{samples[30]['temperature_c']:.2f}",
                "temperature_60_min_c": f"{samples[60]['temperature_c']:.2f}",
                "temperature_120_min_c": f"{samples[120]['temperature_c']:.2f}",
                "initial_pair_heat_into_coffee_w": f"{rows[0]['q_pair_w']:.3f}",
            }
        )
    write_summary(output_dir / "coupled_temperature_summary.csv", summaries)
    plot_results(
        output_dir / "coupled_temperature_evolution.pdf",
        coffee_alone,
        coffee_by_distance,
        coffee_alone_threshold,
    )
    plot_results(
        output_dir / "coupled_temperature_evolution.png",
        coffee_alone,
        coffee_by_distance,
        coffee_alone_threshold,
    )

    for summary in summaries:
        print(summary)


if __name__ == "__main__":
    main()
