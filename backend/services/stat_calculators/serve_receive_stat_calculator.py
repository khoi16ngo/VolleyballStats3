from models.quality import Quality
from models.stats.serve_receive_stats import ServeReceiveStats
from models.user_inputs import UserInputs

def calculate_player_serve_receive_stats(user_inputs: UserInputs, player_raw_serve_receive_stats: dict) -> ServeReceiveStats:
    '''
    Calculate the player serve receive stats from the user inputs and the player raw serve receive stats.
    Returns an ServeReceiveStats object with the calculated stats.
    '''
    player_serve_receive_stats = ServeReceiveStats()
    player_serve_receive_stats.set_perfect_serve_receives(_get_perfect_serve_receives(user_inputs, player_raw_serve_receive_stats))
    player_serve_receive_stats.set_great_serve_receives(_get_great_serve_receives(user_inputs, player_raw_serve_receive_stats))  
    player_serve_receive_stats.set_medium_serve_receives(_get_medium_serve_receives(user_inputs, player_raw_serve_receive_stats))   
    player_serve_receive_stats.set_poor_serve_receives(_get_poor_serve_receives(user_inputs, player_raw_serve_receive_stats))
    player_serve_receive_stats.set_serve_receive_errors(_get_serve_receive_errors(user_inputs, player_raw_serve_receive_stats))
    player_serve_receive_stats.set_total_serve_receives(_get_total_serve_receives(user_inputs, player_raw_serve_receive_stats))
    player_serve_receive_stats.set_in_system_percentage(_get_in_system_percentage(user_inputs, player_raw_serve_receive_stats))
    player_serve_receive_stats.set_out_of_system_percentage(_get_out_of_system_percentage(user_inputs, player_raw_serve_receive_stats))
    player_serve_receive_stats.set_serve_receive_average(_get_serve_receive_average(user_inputs, player_raw_serve_receive_stats))
    return player_serve_receive_stats

def _get_perfect_serve_receives(user_inputs: UserInputs, player_serve_receive_raw_stats: dict) -> int:
    '''
    Get the number of perfect serve receives from the player serve receive stats.
    '''
    return player_serve_receive_raw_stats[user_inputs.perfect_quality.value]

def _get_great_serve_receives(user_inputs: UserInputs, player_serve_receive_raw_stats: dict) -> int:
    '''
    Get the number of great serve receives from the player serve receive stats.
    '''
    return player_serve_receive_raw_stats[user_inputs.good_quality.value]

def _get_medium_serve_receives(user_inputs: UserInputs, player_serve_receive_raw_stats: dict) -> int:
    '''
    Get the number of medium serve receives from the player serve receive stats.
    '''
    return player_serve_receive_raw_stats[user_inputs.ok_quality.value]

def _get_poor_serve_receives(user_inputs: UserInputs, player_serve_receive_raw_stats: dict) -> int:
    '''
    Get the number of poor serve receives from the player serve receive stats.
    '''
    return player_serve_receive_raw_stats[user_inputs.poor_quality.value]

def _get_serve_receive_errors(user_inputs: UserInputs, player_serve_receive_raw_stats: dict) -> int:
    '''
    Get the number of serve receive errors from the player serve receive stats.
    '''
    return player_serve_receive_raw_stats[user_inputs.error_quality.value]

def _get_total_serve_receives(user_inputs: UserInputs, player_raw_serve_receive_stats: dict) -> int:
    '''
    Get the total number of serve receives from the player serve receive stats.
    '''
    perfect_serve_receives = _get_perfect_serve_receives(user_inputs, player_raw_serve_receive_stats)    
    great_serve_receives = _get_great_serve_receives(user_inputs, player_raw_serve_receive_stats)
    medium_serve_receives = _get_medium_serve_receives(user_inputs, player_raw_serve_receive_stats)
    poor_serve_receives = _get_poor_serve_receives(user_inputs, player_raw_serve_receive_stats)
    serve_receive_errors = _get_serve_receive_errors(user_inputs, player_raw_serve_receive_stats)

    return perfect_serve_receives + great_serve_receives + medium_serve_receives + poor_serve_receives + serve_receive_errors

def _get_in_system_percentage(user_inputs: UserInputs, player_raw_serve_receive_stats: dict) -> float:
    '''
    Get the in system percentage from the player serve receive stats.
    The in system percentage is calculated by dividing the total number of serves in system by the total number of serves.
    '''
    total_serve_receives = _get_total_serve_receives(user_inputs, player_raw_serve_receive_stats)
    if total_serve_receives == 0:
        return 0.0
    
    perfect_serve_receives = _get_perfect_serve_receives(user_inputs, player_raw_serve_receive_stats)    
    great_serve_receives = _get_great_serve_receives(user_inputs, player_raw_serve_receive_stats)
    
    return (perfect_serve_receives + great_serve_receives) / total_serve_receives

def _get_out_of_system_percentage(user_inputs: UserInputs, player_raw_serve_receive_stats: dict) -> float:
    '''
    Get the out of system percentage from the player serve receive stats.
    The out of system percentage is calculated by dividing the total number of serves out of system by the total number of serves.
    '''
    total_serve_receives = _get_total_serve_receives(user_inputs, player_raw_serve_receive_stats)
    if total_serve_receives == 0:
        return 0.0
    
    poor_serve_receives = _get_poor_serve_receives(user_inputs, player_raw_serve_receive_stats)    
    
    return poor_serve_receives / total_serve_receives

def _get_serve_receive_average(user_inputs: UserInputs, player_raw_serve_receive_stats: dict) -> float:
    '''
    Get the average of the serve receive stats.
    The average is calculated by weighting the serve_receives with the following weights:
    - Perfect serve receives: 4
    - Great serve receives: 3
    - Good serve receives: 2
    - Poor serve receives: 1
    - Serve receive errors: 0.5
    '''
    total_serve_receives = _get_total_serve_receives(user_inputs, player_raw_serve_receive_stats)
    if total_serve_receives == 0:
        return 0.0
    
    total_weighted_serve_receives = (_get_perfect_serve_receives(user_inputs, player_raw_serve_receive_stats) * 4) + (_get_great_serve_receives(user_inputs, player_raw_serve_receive_stats) * 3) + (_get_medium_serve_receives(user_inputs, player_raw_serve_receive_stats) * 2) + (_get_poor_serve_receives(user_inputs, player_raw_serve_receive_stats) * 1) + (_get_serve_receive_errors(user_inputs, player_raw_serve_receive_stats) * 0.5)
    return total_weighted_serve_receives / total_serve_receives


