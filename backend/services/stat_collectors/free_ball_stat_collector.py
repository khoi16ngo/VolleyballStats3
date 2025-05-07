from models.player_stats import PlayerStats
from models.stats.free_ball_stats import FreeBallStats

def get_free_ball_stats_headers() -> list:
    '''
    Get the headers for the free ball stats.    
    '''
    return [
        'Perfect Free Balls',
        'Great Free Balls',
        'Good Free Balls',
        'Poor Free Balls',
        'Free Ball Errors',
        'Total Free Balls',
        'Free Ball Average',
    ]

def collect_free_ball_stats(player_stats: PlayerStats) -> list:
    '''
    Collect the free ball stats from the player stats.
    '''
    player_free_ball_stats = player_stats.free_ball_stats
    if not isinstance(player_free_ball_stats, FreeBallStats):
        raise ValueError("Player stats is not of type FreeBallStats")
    
    free_ball_stats = []

    free_ball_stats.append(player_free_ball_stats.perfect_free_balls)
    free_ball_stats.append(player_free_ball_stats.great_free_balls)
    free_ball_stats.append(player_free_ball_stats.medium_free_balls)
    free_ball_stats.append(player_free_ball_stats.poor_free_balls)
    free_ball_stats.append(player_free_ball_stats.free_ball_errors)
    free_ball_stats.append(player_free_ball_stats.total_free_balls)
    free_ball_stats.append(player_free_ball_stats.free_ball_average)

    return free_ball_stats
