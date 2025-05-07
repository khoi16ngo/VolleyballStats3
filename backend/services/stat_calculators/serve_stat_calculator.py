from models.quality import Quality
from models.stats.serve_stats import ServeStats
from models.user_inputs import UserInputs

def calculate_player_serve_stats(user_inputs: UserInputs, player_raw_serve_stats: dict) -> ServeStats:
    '''
    Calculate the player serve stats from the user inputs and the player raw serve stats.
    Returns an ServeStats object with the calculated stats.
    '''
    player_serve_stats = ServeStats()
    player_serve_stats.set_aces(_get_perfect_serves(user_inputs, player_raw_serve_stats))
    player_serve_stats.set_great_serves(_get_great_serves(user_inputs, player_raw_serve_stats))  
    player_serve_stats.set_medium_serves(_get_medium_serves(user_inputs, player_raw_serve_stats))   
    player_serve_stats.set_poor_serves(_get_poor_serves(user_inputs, player_raw_serve_stats))
    player_serve_stats.set_serve_errors(_get_serve_errors(user_inputs, player_raw_serve_stats))
    player_serve_stats.set_total_serves(_get_total_serves(user_inputs, player_raw_serve_stats))
    player_serve_stats.set_serve_average(_get_serve_average(user_inputs, player_raw_serve_stats))
    player_serve_stats.set_opponent_in_system_percentage(_get_opponent_in_system_percentage(user_inputs, player_raw_serve_stats))
    player_serve_stats.set_opponent_out_of_system_percentage(_get_opponent_out_of_system_percentage(user_inputs, player_raw_serve_stats))
    return player_serve_stats

def _get_perfect_serves(user_inputs: UserInputs, player_serve_raw_stats: dict) -> int:
    '''
    Get the number of perfect serves from the player serve stats.
    '''
    return player_serve_raw_stats[user_inputs.perfect_quality.value]

def _get_great_serves(user_inputs: UserInputs, player_serve_raw_stats: dict) -> int:
    '''
    Get the number of great serves from the player serve stats.
    '''
    return player_serve_raw_stats[user_inputs.good_quality.value]

def _get_medium_serves(user_inputs: UserInputs, player_serve_raw_stats: dict) -> int:
    '''
    Get the number of medium serves from the player serve stats.
    '''
    return player_serve_raw_stats[user_inputs.ok_quality.value]

def _get_poor_serves(user_inputs: UserInputs, player_serve_raw_stats: dict) -> int:
    '''
    Get the number of poor serves from the player serve stats.
    '''
    return player_serve_raw_stats[user_inputs.poor_quality.value]

def _get_serve_errors(user_inputs: UserInputs, player_serve_raw_stats: dict) -> int:
    '''
    Get the number of serve errors from the player serve stats.
    '''
    return player_serve_raw_stats[user_inputs.error_quality.value]

def _get_total_serves(user_inputs: UserInputs, player_raw_serve_stats: dict) -> int:
    '''
    Get the total number of serves from the player serve stats.
    '''
    perfect_serves = _get_perfect_serves(user_inputs, player_raw_serve_stats)    
    great_serves = _get_great_serves(user_inputs, player_raw_serve_stats)
    medium_serves = _get_medium_serves(user_inputs, player_raw_serve_stats)
    poor_serves = _get_poor_serves(user_inputs, player_raw_serve_stats)
    serve_errors = _get_serve_errors(user_inputs, player_raw_serve_stats)

    return perfect_serves + great_serves + medium_serves + poor_serves + serve_errors

def _get_serve_average(user_inputs: UserInputs, player_raw_serve_stats: dict) -> float:
    '''
    Get the average of the serve stats.
    The average is calculated by weighting the serves with the following weights:
    - Aces: 4
    - Great serves: 3
    - Good serves: 2
    - Poor serves: 1
    - Serve errors: 0.5
    '''
    total_serves = _get_total_serves(user_inputs, player_raw_serve_stats)
    if total_serves == 0:
        return 0.0
    
    total_weighted_serves = (_get_perfect_serves(user_inputs, player_raw_serve_stats) * 4) + (_get_great_serves(user_inputs, player_raw_serve_stats) * 3) + (_get_medium_serves(user_inputs, player_raw_serve_stats) * 2) + (_get_poor_serves(user_inputs, player_raw_serve_stats) * 1) + (_get_serve_errors(user_inputs, player_raw_serve_stats) * 0.5)
    return total_weighted_serves / total_serves

def _get_opponent_in_system_percentage(user_inputs: UserInputs, player_raw_serve_stats: dict) -> float:
    '''
    Get the in system percentage from the player serve stats.
    The in system percentage is calculated by dividing the total number of serves in system by the total number of serves.
    '''
    total_serves = _get_total_serves(user_inputs, player_raw_serve_stats)
    if total_serves == 0:
        return 0.0
    
    perfect_serves = _get_perfect_serves(user_inputs, player_raw_serve_stats)    
    great_serves = _get_great_serves(user_inputs, player_raw_serve_stats)
    
    return (perfect_serves + great_serves) / total_serves

def _get_opponent_out_of_system_percentage(user_inputs: UserInputs, player_raw_serve_stats: dict) -> float:
    '''
    Get the out of system percentage from the player serve stats.
    The out of system percentage is calculated by dividing the total number of serves out of system by the total number of serves.
    '''
    total_serves = _get_total_serves(user_inputs, player_raw_serve_stats)
    if total_serves == 0:
        return 0.0
    
    poor_serves = _get_poor_serves(user_inputs, player_raw_serve_stats)    
    
    return poor_serves / total_serves
