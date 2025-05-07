import re
from utilities.util_file import file_exists, get_file_name_from_file_path, remove_file_extension

def clean_text_file(file_path: str) -> str:
    '''
    Cleans the text file by removing unwanted characters and spaces and creates a new file.
    The line format is cleaned to"{number} {letter} {number}".
    e.g. "12 a 34"
    Returns the cleaned file name.
    '''
    clean_data = []

    if not file_exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    # Open the file and read it line by line
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line == '':
                continue
            
            # Clean line and check if it matches the pattern
            clean_line = _clean_text_line(line)

            if clean_line == '':
                continue

            # Add the cleaned line to the list
            clean_data.append(clean_line)
    
    if len(clean_data) == 0:
        return ""

    new_cleaned_file_name = _get_clean_file_name(file_path)
    # Write to the new cleaned file with the cleaned lines
    with open(new_cleaned_file_name, 'w') as outfile:
        for line in clean_data:
            outfile.write(line + '\n')
    
    return new_cleaned_file_name

LINE_PATTERN_MATCH = r'\d{1,2}\s[a-z]\s\d{1,2}'
def _clean_text_line(line: str) -> str:
    """
    Cleans a line of text by removing unwanted characters and spaces.
    The line format is "{number} {letter} {number}".
    e.g. "12 a 34"
    """
    line = line.strip()
    line_matches = re.findall(LINE_PATTERN_MATCH, line)
    return line_matches[0] if len(line_matches) > 0 else ''

def _get_clean_file_name(file_path: str) -> str:
    """
    Returns the cleaned file name based on the original file path.
    """
    file_name = get_file_name_from_file_path(file_path)
    return "./data/clean_stats/" + remove_file_extension(file_name) + "_cleaned.txt"
