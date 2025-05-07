from models.player_stats import PlayerStats
from models.stats.serve_receive_stats import ServeReceiveStats

def get_serve_receive_stats_headers() -> list:
    '''
    Get the headers for the serve receive stats.
    '''
    return [
        'Perfect Serve Receive Passes',
        'Great Serve Receive Passes',
        'Good Serve Receive Passes',
        'Poor Serve Receive Passes',
        'Serve Receive Pass Errors',
        'Total Serve Receive Passes',
        'Serve Receive Pass Average',
        'In System %',
        'Out of System %',
    ]

def collect_serve_receive_stats(player_stats: PlayerStats) -> list:
    '''
    Collect the serve receive stats from the player stats.
    '''
    player_serve_receive_stats = player_stats.serve_receive_stats
    if not isinstance(player_serve_receive_stats, ServeReceiveStats):
        raise ValueError("Player stats is not of type ServeReceiveStats")

    serve_receive_stats = []

    serve_receive_stats.append(player_serve_receive_stats.perfect_serve_receives)
    serve_receive_stats.append(player_serve_receive_stats.great_serve_receives)
    serve_receive_stats.append(player_serve_receive_stats.medium_serve_receives)
    serve_receive_stats.append(player_serve_receive_stats.poor_serve_receives)
    serve_receive_stats.append(player_serve_receive_stats.serve_receive_errors)
    serve_receive_stats.append(player_serve_receive_stats.total_serve_receives)
    serve_receive_stats.append(player_serve_receive_stats.serve_receive_average)
    serve_receive_stats.append(player_serve_receive_stats.in_system_percentage)
    serve_receive_stats.append(player_serve_receive_stats.out_of_system_percentage)
    
    return serve_receive_stats
