import csv


def save_to_csv(x_data: list[float], y_data: list[float], file_name: str) -> None:
    """
    - save the input data to a csv file
    """
    data_pre_path = '../data'
    with open(f'{data_pre_path}/{file_name}.csv', 'w+', encoding='UTF8') as handler:
        writer = csv.writer(handler)
        writer.writerow([f'idx', 'q', 'V(q)'])
        for idx in range(len(x_data)):
            writer.writerow([idx+1, x_data[idx], y_data[idx]])
