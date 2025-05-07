import sys
from models import user_inputs
from program import Program
from services.user_prompters.action_prompter import askForActions
from services.user_prompters.file_prompter import askForRawFiles
from services.user_prompters.player_prompter import askForPlayers
from services.user_prompters.quality_prompter import askForQualities
from models.constants.action_qualities import *
from models.constants.action_types import *

if __name__ == "__main__":
    players = askForPlayers()
    if len(players) == 0:
        print("No players entered. Exiting program.")
        sys.exit(1)
    
    qualities = askForQualities()
    if len(qualities) == 0:
        print("No qualities entered. Exiting program.")
        sys.exit(1)

    actions = askForActions()
    if len(actions) == 0:
        print("No actions entered. Exiting program.")
        sys.exit(1)

    raw_data_file_paths = askForRawFiles()
    if len(raw_data_file_paths) == 0:  
        print("No CSV files entered. Exiting program.")
        sys.exit(1)

    user_inputs = user_inputs.UserInputs(players, actions, qualities, raw_data_file_paths)
    program = Program(user_inputs)
    program.run()