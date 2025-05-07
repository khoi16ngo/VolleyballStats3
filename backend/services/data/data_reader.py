def read_data_file(file_path: str) -> list:
    """
    Reads a data file and returns a list of lines.
    Each line is stripped of leading and trailing whitespace.
    Empty lines are ignored.
    """
    clean_data = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line == '':
                continue
            clean_data.append(line)
    
    return clean_data