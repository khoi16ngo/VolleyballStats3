from models.quality import Quality
from models.stats.dig_stats import DigStats
from models.user_inputs import UserInputs

def calculate_player_dig_stats(user_inputs: UserInputs, player_raw_dig_stats: dict) -> DigStats:
    '''
    Calculate the player dig stats from the user inputs and the player raw dig stats.
    Returns an DigStats object with the calculated stats.
    '''
    player_dig_stats = DigStats()
    player_dig_stats.set_perfect_digs(_get_perfect_digs(user_inputs, player_raw_dig_stats))
    player_dig_stats.set_great_digs(_get_great_digs(user_inputs, player_raw_dig_stats))  
    player_dig_stats.set_medium_digs(_get_medium_digs(user_inputs, player_raw_dig_stats))   
    player_dig_stats.set_poor_digs(_get_poor_digs(user_inputs, player_raw_dig_stats))
    player_dig_stats.set_dig_errors(_get_dig_errors(user_inputs, player_raw_dig_stats))
    player_dig_stats.set_total_digs(_get_total_digs(user_inputs, player_raw_dig_stats))
    player_dig_stats.set_dig_average(_get_dig_average(user_inputs, player_raw_dig_stats))
    return player_dig_stats

def _get_perfect_digs(user_inputs: UserInputs, player_dig_raw_stats: dict) -> int:
    '''
    Get the number of perfect digs from the player dig stats.
    '''
    return player_dig_raw_stats[user_inputs.perfect_quality.value]

def _get_great_digs(user_inputs: UserInputs, player_dig_raw_stats: dict) -> int:
    '''
    Get the number of great digs from the player dig stats.
    '''
    return player_dig_raw_stats[user_inputs.good_quality.value]

def _get_medium_digs(user_inputs: UserInputs, player_dig_raw_stats: dict) -> int:
    '''
    Get the number of medium digs from the player dig stats.
    '''
    return player_dig_raw_stats[user_inputs.ok_quality.value]

def _get_poor_digs(user_inputs: UserInputs, player_dig_raw_stats: dict) -> int:
    '''
    Get the number of poor digs from the player dig stats.
    '''
    return player_dig_raw_stats[user_inputs.poor_quality.value]

def _get_dig_errors(user_inputs: UserInputs, player_dig_raw_stats: dict) -> int:
    '''
    Get the number of dig errors from the player dig stats.
    '''
    return player_dig_raw_stats[user_inputs.error_quality.value]

def _get_total_digs(user_inputs: UserInputs, player_raw_dig_stats: dict) -> int:
    '''
    Get the total number of digs from the player dig stats.
    '''
    perfect_digs = _get_perfect_digs(user_inputs, player_raw_dig_stats)    
    great_digs = _get_great_digs(user_inputs, player_raw_dig_stats)
    medium_digs = _get_medium_digs(user_inputs, player_raw_dig_stats)
    poor_digs = _get_poor_digs(user_inputs, player_raw_dig_stats)
    dig_errors = _get_dig_errors(user_inputs, player_raw_dig_stats)

    return perfect_digs + great_digs + medium_digs + poor_digs + dig_errors

def _get_dig_average(user_inputs: UserInputs, player_raw_dig_stats: dict) -> float:
    '''
    Get the average of the dig stats.
    The average is calculated by weighting the digs with the following weights:
    - Perfect digs: 4
    - Great digs: 3
    - Good digs: 2
    - Poor digs: 1
    - Dig errors: 0.5
    '''
    total_digs = _get_total_digs(user_inputs, player_raw_dig_stats)
    if total_digs == 0:
        return 0.0
    
    total_weighted_digs = (_get_perfect_digs(user_inputs, player_raw_dig_stats) * 4) + (_get_great_digs(user_inputs, player_raw_dig_stats) * 3) + (_get_medium_digs(user_inputs, player_raw_dig_stats) * 2) + (_get_poor_digs(user_inputs, player_raw_dig_stats) * 1) + (_get_dig_errors(user_inputs, player_raw_dig_stats) * 0.5)
    return total_weighted_digs / total_digs


