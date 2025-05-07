from models.player_stats import PlayerStats
from models.stats.assist_stats import AssistStats

def get_assist_stats_headers() -> list:
    '''
    Get the headers for the assist stats.
    '''
    return [
        'Perfect Assists',
        'Great Assists',
        'Good Assists',
        'Poor Assists', 
        'Assist Errors',
        'Total Assists',
        'Assist Average',
    ]

def collect_assist_stats(player_stats: PlayerStats) -> list:
    '''
    Collect the assist stats from the player stats.
    '''
    player_assist_stats = player_stats.assist_stats
    if not isinstance(player_assist_stats, AssistStats):
        raise ValueError("Player stats is not of type AssistStats")
    
    assist_stats = []

    assist_stats.append(player_assist_stats.perfect_assists)
    assist_stats.append(player_assist_stats.great_assists)
    assist_stats.append(player_assist_stats.medium_assists)
    assist_stats.append(player_assist_stats.poor_assists)
    assist_stats.append(player_assist_stats.assist_errors)
    assist_stats.append(player_assist_stats.total_assists)
    assist_stats.append(player_assist_stats.assist_average)

    return assist_stats