import csv

def print_stats_csv(file_path: str, data: list):
    '''
    Write the given data to a CSV file at the specified file path.
    The first row of the data should contain the headers.
    '''
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)