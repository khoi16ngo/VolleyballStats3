
from models.player_stats import PlayerStats
from models.stats.serve_stats import ServeStats


def get_serve_stats_headers() -> list:
    '''
    Get the headers for the serve stats.
    '''
    return [
        'Aces',
        'Great Serves',
        'Good Serves',
        'Poor Serves',
        'Serve Errors',
        'Total Serves',
        'Serve Average',
        'Opponent Out of System %',
    ]

def collect_serve_stats(player_stats: PlayerStats) -> list:
    '''
    Collect the serve stats from the player stats.
    '''
    player_serve_stats = player_stats.serve_stats
    if not isinstance(player_serve_stats, ServeStats):
        raise ValueError("Player stats is not of type ServeStats")
    
    serve_stats = []

    serve_stats.append(player_serve_stats.aces)
    serve_stats.append(player_serve_stats.great_serves)
    serve_stats.append(player_serve_stats.medium_serves)
    serve_stats.append(player_serve_stats.poor_serves)
    serve_stats.append(player_serve_stats.serve_errors)
    serve_stats.append(player_serve_stats.total_serves)
    serve_stats.append(player_serve_stats.serve_average)
    serve_stats.append(player_serve_stats.opponent_out_of_system_percentage)

    return serve_stats
