from models.constants.action_qualities import ALL_QUALITIES
from models.quality import Quality

def askForQualities() -> list:
    """
    Prompt the user for the qualities for a volleyball action.
    Returns a list of Quality object.
    """
    
    qualities = []
    print("Please enter the qualities for a volleyball action.")
    for quality in ALL_QUALITIES:
        while True:
            # Get quality value
            value = input(f"Enter quality value, must be a number, for {quality}: ").strip()
            if quality == "":
                print("No action entered. Please try again.")
                continue
            elif not value.isnumeric():
                print("Invalid quality value entered. Must be a number. Please try again.")
                continue
            elif int(value) >= 100 or int(value) < 0:
                print("Invalid quality value entered. Must be between 0 and 100. Please try again.")
                continue

            # Add quality to list
            qualities.append(Quality(quality, int(value)))
            break
    
    return qualities