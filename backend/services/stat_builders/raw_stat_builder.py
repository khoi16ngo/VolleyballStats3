from models.user_inputs import UserInputs

def build_raw_player_stats(user_inputs: UserInputs, raw_player_stats: list) -> dict:
    '''
    Calculate the raw player stats from the raw player stats file.
    The raw player stats file is a list of strings in the format "<player_number> <action> <quality>".
    e.g. "12 a 34"
    Returns a dictionary with the player number as the key and a dictionary of actions and qualities as the value.
    The dictionary will be in the format:
    {
        <player.number>: {
            "actions": {
                <action.value>: {
                    "qualities": {11
                        <quality.value>: count
                    }
                } 
            }
        }
    }
    '''
    # Initialize player stat dict with all actions and qualities at count 0
    calculated_player_stats = {
        player.number: {
            "actions": {
                action.value: {
                    "qualities": {
                        quality.value: 0
                        for quality in user_inputs.action_qualities
                    }
                }
                for action in user_inputs.actions
            }
        }
        for player in user_inputs.players
    }

    # Loop through each line in the raw player stats list and then add to the count for the action and quality
    for raw_player_stat in raw_player_stats:
        # Split each line into format "<play_number> <action> <quality>"
        raw_player_number, action, raw_quality = raw_player_stat.strip().split()
        player_number = int(raw_player_number)
        quality = int(raw_quality)

        # Increase count by one if action and quality performed for player
        if not player_number in calculated_player_stats:
            print(f"Player number {player_number} was not inputted originally, ignoring raw data line")
            continue
        elif not action in calculated_player_stats[player_number]["actions"]:
            print(f"Action {action} was not inputted originally, ignoring raw data line")
            continue
        elif not quality in calculated_player_stats[player_number]["actions"][action]["qualities"]:
            print(f"Quality {quality} was not inputted originally, ignoring raw data line")
            continue

        calculated_player_stats[player_number]["actions"][action]["qualities"][quality] += 1
        
    return calculated_player_stats    

def fetch_player_raw_assist_stats(user_inputs: UserInputs, player_number: int, calculated_player_stats: dict) -> dict:
    '''
    Fetch the player assist stats from the calculated player stats.
    The calculated player stats is a dictionary with the player number as the key and a dictionary of actions and qualities as the value.
    The dictionary will be in the format:
    {
        <player.number>: {
            "actions": {
                <action.value>: {
                    "qualities": {
                        <quality.value>: count
                    }
                } 
            }
        }
    }
    '''
    if player_number not in calculated_player_stats:
        raise ValueError(f"Player number {player_number} not found in calculated player stats.")
    elif user_inputs.assist_action is None:
        raise ValueError("Assist action not found in user inputs.")
    

    return calculated_player_stats[player_number]["actions"][user_inputs.assist_action.value]["qualities"]

def fetch_player_raw_attack_stats(user_inputs: UserInputs, player_number: int, calculated_player_stats: dict) -> dict:
    '''
    Fetch the player attack stats from the calculated player stats.
    The calculated player stats is a dictionary with the player number as the key and a dictionary of actions and qualities as the value.
    The dictionary will be in the format:
    {
        <player.number>: {
            "actions": {
                <action.value>: {
                    "qualities": {
                        <quality.value>: count
                    }
                } 
            }
        }
    }
    '''
    if player_number not in calculated_player_stats:
        raise ValueError(f"Player number {player_number} not found in calculated player stats.")
    elif user_inputs.attack_action is None:
        raise ValueError("Attack action not found in user inputs.")
    
    return calculated_player_stats[player_number]["actions"][user_inputs.attack_action.value]["qualities"]

def fetch_player_raw_block_stats(user_inputs: UserInputs, player_number: int, calculated_player_stats: dict) -> dict:
    '''
    Fetch the player block stats from the calculated player stats.
    The calculated player stats is a dictionary with the player number as the key and a dictionary of actions and qualities as the value.
    The dictionary will be in the format:
    {
        <player.number>: {
            "actions": {
                <action.value>: {
                    "qualities": {
                        <quality.value>: count
                    }
                } 
            }
        }
    }
    '''
    if player_number not in calculated_player_stats:
        raise ValueError(f"Player number {player_number} not found in calculated player stats.")
    elif user_inputs.block_action is None:
        raise ValueError("Block action not found in user inputs.")
    
    return calculated_player_stats[player_number]["actions"][user_inputs.block_action.value]["qualities"]

def fetch_player_raw_dig_stats(user_inputs: UserInputs, player_number: int, calculated_player_stats: dict) -> dict:
    '''
    Fetch the player dig stats from the calculated player stats.
    The calculated player stats is a dictionary with the player number as the key and a dictionary of actions and qualities as the value.
    The dictionary will be in the format:
    {
        <player.number>: {
            "actions": {
                <action.value>: {
                    "qualities": {
                        <quality.value>: count
                    }
                } 
            }
        }
    }
    '''
    if player_number not in calculated_player_stats:
        raise ValueError(f"Player number {player_number} not found in calculated player stats.")
    elif user_inputs.dig_action is None:
        raise ValueError("Dig action not found in user inputs.")
    
    return calculated_player_stats[player_number]["actions"][user_inputs.dig_action.value]["qualities"]

def fetch_player_raw_free_ball_stats(user_inputs: UserInputs, player_number: int, calculated_player_stats: dict) -> dict:
    '''
    Fetch the player free ball stats from the calculated player stats.
    The calculated player stats is a dictionary with the player number as the key and a dictionary of actions and qualities as the value.
    The dictionary will be in the format:
    {
        <player.number>: {
            "actions": {
                <action.value>: {
                    "qualities": {
                        <quality.value>: count
                    }
                } 
            }
        }
    }
    '''
    if player_number not in calculated_player_stats:
        raise ValueError(f"Player number {player_number} not found in calculated player stats.")
    elif user_inputs.free_ball_action is None:
        raise ValueError("Free ball action not found in user inputs.")
    
    return calculated_player_stats[player_number]["actions"][user_inputs.free_ball_action.value]["qualities"]

def fetch_player_raw_serve_receive_stats(user_inputs: UserInputs, player_number: int, calculated_player_stats: dict) -> dict:
    '''
    Fetch the player serve receive stats from the calculated player stats.
    The calculated player stats is a dictionary with the player number as the key and a dictionary of actions and qualities as the value.
    The dictionary will be in the format:
    {
        <player.number>: {
            "actions": {
                <action.value>: {
                    "qualities": {
                        <quality.value>: count
                    }
                } 
            }
        }
    }
    '''
    if player_number not in calculated_player_stats:
        raise ValueError(f"Player number {player_number} not found in calculated player stats.")
    elif user_inputs.serve_receive_pass_action is None:
        raise ValueError("Serve receive action not found in user inputs.")
    
    return calculated_player_stats[player_number]["actions"][user_inputs.serve_receive_pass_action.value]["qualities"]

def fetch_player_raw_serve_stats(user_inputs: UserInputs, player_number: int, calculated_player_stats: dict) -> dict:
    '''
    Fetch the player serve stats from the calculated player stats.
    The calculated player stats is a dictionary with the player number as the key and a dictionary of actions and qualities as the value.
    The dictionary will be in the format:
    {
        <player.number>: {
            "actions": {
                <action.value>: {
                    "qualities": {
                        <quality.value>: count
                    }
                } 
            }
        }
    }
    '''
    if player_number not in calculated_player_stats:
        raise ValueError(f"Player number {player_number} not found in calculated player stats.")
    elif user_inputs.serve_action is None:
        raise ValueError("Serve action not found in user inputs.")
    
    return calculated_player_stats[player_number]["actions"][user_inputs.serve_action.value]["qualities"]