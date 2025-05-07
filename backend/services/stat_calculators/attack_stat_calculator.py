from models.quality import Quality
from models.stats.attack_stats import AttackStats
from models.user_inputs import UserInputs

def calculate_player_attack_stats(user_inputs: UserInputs, player_attack_raw_stats: dict) -> AttackStats:
    '''
    Calculate the player attack stats from the user inputs and the player attack raw stats.
    Returns an AttackStats object with the calculated stats.
    '''
    player_attack_stats = AttackStats()
    player_attack_stats.set_kills(_get_kills(user_inputs, player_attack_raw_stats))
    player_attack_stats.set_great_attacks(_get_great_attacks(user_inputs, player_attack_raw_stats))  
    player_attack_stats.set_medium_attacks(_get_medium_attacks(user_inputs, player_attack_raw_stats))   
    player_attack_stats.set_poor_attacks(_get_poor_attacks(user_inputs, player_attack_raw_stats))
    player_attack_stats.set_attack_errors(_get_attack_errors(user_inputs, player_attack_raw_stats))
    player_attack_stats.set_total_attacks(_get_total_attacks(user_inputs, player_attack_raw_stats))
    player_attack_stats.set_hitting_average(_get_hitting_average(user_inputs, player_attack_raw_stats))
    player_attack_stats.set_kill_percentage(_get_kill_percentage(user_inputs, player_attack_raw_stats))
    player_attack_stats.set_hitting_percentage(_get_hitting_percentage(user_inputs, player_attack_raw_stats))
    return player_attack_stats

def _get_kills(user_inputs: UserInputs, player_attack_raw_stats: dict) -> int:
    '''
    Get the number of perfect attacks from the player attack stats.
    '''
    return player_attack_raw_stats[user_inputs.perfect_quality.value]

def _get_great_attacks(user_inputs: UserInputs, player_attack_raw_stats: dict) -> int:
    '''
    Get the number of great attacks from the player attack stats.
    '''
    return player_attack_raw_stats[user_inputs.good_quality.value]

def _get_medium_attacks(user_inputs: UserInputs, player_attack_raw_stats: dict) -> int:
    '''
    Get the number of medium attacks from the player attack stats.
    '''
    return player_attack_raw_stats[user_inputs.ok_quality.value]

def _get_poor_attacks(user_inputs: UserInputs, player_attack_raw_stats: dict) -> int:
    '''
    Get the number of poor attacks from the player attack stats.
    '''
    return player_attack_raw_stats[user_inputs.poor_quality.value]

def _get_attack_errors(user_inputs: UserInputs, player_attack_raw_stats: dict) -> int:
    '''
    Get the number of attack errors from the player attack stats.
    '''
    return player_attack_raw_stats[user_inputs.error_quality.value]

def _get_total_attacks(user_inputs: UserInputs, player_attack_raw_stats: dict) -> int:
    '''
    Get the total number of attacks from the player attack stats.
    '''
    perfect_attacks = _get_kills(user_inputs, player_attack_raw_stats)    
    great_attacks = _get_great_attacks(user_inputs, player_attack_raw_stats)
    medium_attacks = _get_medium_attacks(user_inputs, player_attack_raw_stats)
    poor_attacks = _get_poor_attacks(user_inputs, player_attack_raw_stats)
    attack_errors = _get_attack_errors(user_inputs, player_attack_raw_stats)

    return perfect_attacks + great_attacks + medium_attacks + poor_attacks + attack_errors

def _get_hitting_percentage(user_inputs: UserInputs, player_attack_raw_stats: dict) -> float:
    '''
    Get the hitting percentage of the player.
    The hitting percentage is calculated as follows:
    (kills - attack_errors) / total_attacks
    '''
    total_attacks = _get_total_attacks(user_inputs, player_attack_raw_stats)
    if total_attacks == 0:
        return 0.0
    
    kills = _get_kills(user_inputs, player_attack_raw_stats)
    attack_errors = _get_attack_errors(user_inputs, player_attack_raw_stats)
    return (kills - attack_errors) / total_attacks

def _get_kill_percentage(user_inputs: UserInputs, player_attack_raw_stats: dict) -> float:
    '''
    Get the kill percentage of the player.
    The kill percentage is calculated as follows:
    kills / total_attacks
    '''
    total_attacks = _get_total_attacks(user_inputs, player_attack_raw_stats)
    if total_attacks == 0:
        return 0.0
    
    kills = _get_kills(user_inputs, player_attack_raw_stats)
    return kills / total_attacks

def _get_hitting_average(user_inputs: UserInputs, player_attack_raw_stats: dict) -> float:
    '''
    Get the average of the attack stats.
    The average is calculated by weighting the attacks with the following weights:
    - Kills: 4
    - Great attacks: 3
    - Good attacks: 2
    - Poor attacks: 1
    - Attack errors: 0.5
    '''
    total_attacks = _get_total_attacks(user_inputs, player_attack_raw_stats)
    if total_attacks == 0:
        return 0.0
    
    total_weighted_attacks = (_get_kills(user_inputs, player_attack_raw_stats) * 4) + (_get_great_attacks(user_inputs, player_attack_raw_stats) * 3) + (_get_medium_attacks(user_inputs, player_attack_raw_stats) * 2) + (_get_poor_attacks(user_inputs, player_attack_raw_stats) * 1) + (_get_attack_errors(user_inputs, player_attack_raw_stats) * 0.5)
    return total_weighted_attacks /total_attacks


