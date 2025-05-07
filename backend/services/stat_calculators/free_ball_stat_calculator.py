from models.quality import Quality
from models.stats.free_ball_stats import FreeBallStats
from models.user_inputs import UserInputs

def calculate_player_free_ball_stats(user_inputs: UserInputs, player_raw_free_ball_stats: dict) -> FreeBallStats:
    '''
    Calculate the player free ball stats from the user inputs and the player raw free ball stats.
    Returns an FreeBallStats object with the calculated stats.
    '''
    player_free_ball_stats = FreeBallStats()
    player_free_ball_stats.set_perfect_free_balls(_get_perfect_free_balls(user_inputs, player_raw_free_ball_stats))
    player_free_ball_stats.set_great_free_balls(_get_great_free_balls(user_inputs, player_raw_free_ball_stats))  
    player_free_ball_stats.set_medium_free_balls(_get_medium_free_balls(user_inputs, player_raw_free_ball_stats))   
    player_free_ball_stats.set_poor_free_balls(_get_poor_free_balls(user_inputs, player_raw_free_ball_stats))
    player_free_ball_stats.set_free_ball_errors(_get_free_ball_errors(user_inputs, player_raw_free_ball_stats))
    player_free_ball_stats.set_total_free_balls(_get_total_free_balls(user_inputs, player_raw_free_ball_stats))
    player_free_ball_stats.set_free_ball_average(_get_free_ball_average(user_inputs, player_raw_free_ball_stats))
    return player_free_ball_stats

def _get_perfect_free_balls(user_inputs: UserInputs, player_free_ball_raw_stats: dict) -> int:
    '''
    Get the number of perfect free balls from the player free ball stats.
    '''
    return player_free_ball_raw_stats[user_inputs.perfect_quality.value]

def _get_great_free_balls(user_inputs: UserInputs, player_free_ball_raw_stats: dict) -> int:
    '''
    Get the number of great free balls from the player free ball stats.
    '''
    return player_free_ball_raw_stats[user_inputs.good_quality.value]

def _get_medium_free_balls(user_inputs: UserInputs, player_free_ball_raw_stats: dict) -> int:
    '''
    Get the number of medium free balls from the player free ball stats.
    '''
    return player_free_ball_raw_stats[user_inputs.ok_quality.value]

def _get_poor_free_balls(user_inputs: UserInputs, player_free_ball_raw_stats: dict) -> int:
    '''
    Get the number of poor free balls from the player free ball stats.
    '''
    return player_free_ball_raw_stats[user_inputs.poor_quality.value]

def _get_free_ball_errors(user_inputs: UserInputs, player_free_ball_raw_stats: dict) -> int:
    '''
    Get the number of free ball errors from the player free ball stats.
    '''
    return player_free_ball_raw_stats[user_inputs.error_quality.value]

def _get_total_free_balls(user_inputs: UserInputs, player_raw_free_ball_stats: dict) -> int:
    '''
    Get the total number of free balls from the player free ball stats.
    '''
    perfect_free_balls = _get_perfect_free_balls(user_inputs, player_raw_free_ball_stats)    
    great_free_balls = _get_great_free_balls(user_inputs, player_raw_free_ball_stats)
    medium_free_balls = _get_medium_free_balls(user_inputs, player_raw_free_ball_stats)
    poor_free_balls = _get_poor_free_balls(user_inputs, player_raw_free_ball_stats)
    free_ball_errors = _get_free_ball_errors(user_inputs, player_raw_free_ball_stats)

    return perfect_free_balls + great_free_balls + medium_free_balls + poor_free_balls + free_ball_errors

def _get_free_ball_average(user_inputs: UserInputs, player_raw_free_ball_stats: dict) -> float:
    '''
    Get the average of the free ball stats.
    The average is calculated by weighting the free balls with the following weights:
    - Perfect free balls: 4
    - Great free balls: 3
    - Good free balls: 2
    - Poor free balls: 1
    - Free ball errors: 0.5
    '''
    total_free_balls = _get_total_free_balls(user_inputs, player_raw_free_ball_stats)
    if total_free_balls == 0:
        return 0.0
    
    total_weighted_free_balls = (_get_perfect_free_balls(user_inputs, player_raw_free_ball_stats) * 4) + (_get_great_free_balls(user_inputs, player_raw_free_ball_stats) * 3) + (_get_medium_free_balls(user_inputs, player_raw_free_ball_stats) * 2) + (_get_poor_free_balls(user_inputs, player_raw_free_ball_stats) * 1) + (_get_free_ball_errors(user_inputs, player_raw_free_ball_stats) * 0.5)
    return total_weighted_free_balls / total_free_balls


