from models.quality import Quality
from models.stats.assist_stats import AssistStats
from models.user_inputs import UserInputs

def calculate_player_assist_stats(user_inputs: UserInputs, player_raw_assist_stats: dict) -> AssistStats:
    '''
    Calculate the player assist stats from the user inputs and the player raw assist stats.
    Returns an AssistStats object with the calculated stats.
    '''
    player_assist_stats = AssistStats()
    player_assist_stats.set_perfect_assists(_get_perfect_assists(user_inputs, player_raw_assist_stats))
    player_assist_stats.set_great_assists(_get_great_assists(user_inputs, player_raw_assist_stats))  
    player_assist_stats.set_medium_assists(_get_medium_assists(user_inputs, player_raw_assist_stats))   
    player_assist_stats.set_poor_assists(_get_poor_assists(user_inputs, player_raw_assist_stats))
    player_assist_stats.set_assist_errors(_get_assist_errors(user_inputs, player_raw_assist_stats))
    player_assist_stats.set_total_assists(_get_total_assists(user_inputs, player_raw_assist_stats))
    player_assist_stats.set_assist_average(_get_assist_average(user_inputs, player_raw_assist_stats))
    return player_assist_stats

def _get_perfect_assists(user_inputs: UserInputs, player_assist_raw_stats: dict) -> int:
    '''
    Get the number of perfect assists from the player assist stats.
    '''
    return player_assist_raw_stats[user_inputs.perfect_quality.value]

def _get_great_assists(user_inputs: UserInputs, player_assist_raw_stats: dict) -> int:
    '''
    Get the number of great assists from the player assist stats.
    '''
    return player_assist_raw_stats[user_inputs.good_quality.value]

def _get_medium_assists(user_inputs: UserInputs, player_assist_raw_stats: dict) -> int:
    '''
    Get the number of medium assists from the player assist stats.
    '''
    return player_assist_raw_stats[user_inputs.ok_quality.value]

def _get_poor_assists(user_inputs: UserInputs, player_assist_raw_stats: dict) -> int:
    '''
    Get the number of poor assists from the player assist stats.
    '''
    return player_assist_raw_stats[user_inputs.poor_quality.value]

def _get_assist_errors(user_inputs: UserInputs, player_assist_raw_stats: dict) -> int:
    '''
    Get the number of assist errors from the player assist stats.
    '''
    return player_assist_raw_stats[user_inputs.error_quality.value]

def _get_total_assists(user_inputs: UserInputs, player_raw_assist_stats: dict) -> int:
    '''
    Get the total number of assists from the player assist stats.
    '''
    perfect_assists = _get_perfect_assists(user_inputs, player_raw_assist_stats)    
    great_assists = _get_great_assists(user_inputs, player_raw_assist_stats)
    medium_assists = _get_medium_assists(user_inputs, player_raw_assist_stats)
    poor_assists = _get_poor_assists(user_inputs, player_raw_assist_stats)
    assist_errors = _get_assist_errors(user_inputs, player_raw_assist_stats)

    return perfect_assists + great_assists + medium_assists + poor_assists + assist_errors

def _get_assist_average(user_inputs: UserInputs, player_raw_assist_stats: dict) -> float:
    '''
    Get the average of the assist stats.
    The average is calculated by weighting the assists with the following weights:
    - Aces: 4
    - Great serves: 3
    - Good serves: 2
    - Poor serves: 1
    - Serve errors: 0.5
    '''
    total_assists = _get_total_assists(user_inputs, player_raw_assist_stats)
    if total_assists == 0:
        return 0.0
    
    total_weighted_assists = (_get_perfect_assists(user_inputs, player_raw_assist_stats) * 4) + (_get_great_assists(user_inputs, player_raw_assist_stats) * 3) + (_get_medium_assists(user_inputs, player_raw_assist_stats) * 2) + (_get_poor_assists(user_inputs, player_raw_assist_stats) * 1) + (_get_assist_errors(user_inputs, player_raw_assist_stats) * 0.5)
    return total_weighted_assists / total_assists


