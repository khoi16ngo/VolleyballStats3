import os

def askForRawFiles() -> list:
    """
    Asks the user for the raw data file path.
    Returns list of raw data file paths.
    """

    file_paths = []
    while True:
        # Ask for the file paths
        file_path = input("Please enter the path to your raw data file: ")

        # Check if the file exists
        while not os.path.isfile(file_path):
            print("The file does not exist. Please try again.")
            file_path = input("Please enter the path to your raw data file: ")

        # Add file path to list
        file_paths.append(file_path)
        
        # Ask if there are more files
        while True:
            exit = input("Are there more files? (y/n): ").strip().lower()
            if exit == "y":
                break
            elif exit == "n":
                return file_paths
            else:
                print("Invalid input. Please enter 'y' or 'n'.")