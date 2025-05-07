from models.action import Action
from models.constants.action_types import ALL_ACTIONS


def askForActions() -> list:
    """
    Prompt the user for the volleyball actions.
    Returns a list of Action object.
    """
    
    actions = []
    print("Please enter the volleyball actions.")
    for action in ALL_ACTIONS:
        while True:
            # Get action value
            alias = input(f"Enter action alias, must be a single alphabet letter, for {action}: ").strip().lower()
            if alias == "":
                print("No action entered. Please try again.")
                continue
            elif len(alias) != 1 or not alias.isalpha():
                print("Invalid action entered. Must be a single alphabet letter. Please try again.")
                continue

            # Add action to list
            actions.append(Action(action, alias))
            break

    return actions