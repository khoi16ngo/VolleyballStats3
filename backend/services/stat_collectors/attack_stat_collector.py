
from models.player_stats import PlayerStats
from models.stats.attack_stats import AttackStats

def get_attack_stats_headers() -> list:
    '''
    Get the headers for the attack stats.
    '''
    return [
        'Kills',
        'Great Attacks',
        'Good Attacks',
        'Poor Attacks',
        'Attack Errors',
        'Total Attacks',
        'Hitting Average', 
        'Kill %',
        'Hitting %',
    ]

def collect_attack_stats(player_stats: PlayerStats) -> list:
    '''
    Collect the attack stats from the player stats.
    '''
    player_attack_stats = player_stats.attack_stats
    if not isinstance(player_attack_stats, AttackStats):
        raise ValueError("Player stats is not of type AttackStats")
    attack_stats = []

    attack_stats.append(player_attack_stats.kills)
    attack_stats.append(player_attack_stats.great_attacks)
    attack_stats.append(player_attack_stats.medium_attacks)
    attack_stats.append(player_attack_stats.poor_attacks)
    attack_stats.append(player_attack_stats.attack_errors)
    attack_stats.append(player_attack_stats.total_attacks)

    attack_stats.append(player_attack_stats.hitting_average)
    attack_stats.append(player_attack_stats.kill_percentage)
    attack_stats.append(player_attack_stats.hitting_average)

    return attack_stats
