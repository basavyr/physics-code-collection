import csv
import os
DATA_DIR = '../data'


def export_to_csv(data: list[tuple], file_name: str, header: tuple) -> None:
    """
    - take the entire data set and exports it to a csv file
    """
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(os.path.join(DATA_DIR, f'{file_name}.csv'), 'w+') as handler:
        csv_writer = csv.writer(handler)
        csv_writer.writerow(header)
        for row in data:
            csv_writer.writerow(row)
