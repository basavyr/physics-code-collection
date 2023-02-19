import csv


def save_to_csv(data: list[tuple], file_name: str, header: list[str]) -> None:
    """
    - save the input data to a csv file
    """
    data_pre_path = '../data'
    with open(f'{data_pre_path}/{file_name}.csv', 'w+', encoding='UTF8') as handler:
        writer = csv.writer(handler)
        writer.writerow(header)
        for row in data:
            writer.writerow(row)
