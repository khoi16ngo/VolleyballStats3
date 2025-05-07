
from models.player_stats import PlayerStats
from models.stats.dig_stats import DigStats

def get_dig_stats_headers() -> list:
    '''
    Get the headers for the dig stats.
    '''
    return [
        'Perfect Digs',
        'Great Digs',
        'Good Digs',
        'Poor Digs',
        'Dig Errors',
        'Total Digs',
        'Dig Average',
    ]

def collect_dig_stats(player_stats: PlayerStats) -> list:
    '''
    Collect the dig stats from the player stats.
    '''
    player_dig_stats = player_stats.dig_stats
    if not isinstance(player_dig_stats, DigStats):
        raise ValueError("Player stats is not of type DigStats")

    dig_stats = []

    dig_stats.append(player_dig_stats.perfect_digs)
    dig_stats.append(player_dig_stats.great_digs)
    dig_stats.append(player_dig_stats.medium_digs)
    dig_stats.append(player_dig_stats.poor_digs)
    dig_stats.append(player_dig_stats.dig_errors)
    dig_stats.append(player_dig_stats.total_digs)
    dig_stats.append(player_dig_stats.dig_average)

    return dig_stats
