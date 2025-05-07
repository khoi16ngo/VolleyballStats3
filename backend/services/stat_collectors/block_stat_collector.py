from models.player_stats import PlayerStats
from models.stats.block_stats import BlockStats
def get_block_stats_headers() -> list:
    return [
        'Perfect Blocks',
        'Great Blocks',
        'Good Blocks',
        'Poor Blocks',
        'Block Errors', 
        'Total Blocks',
        'Block Average',
    ]

def collect_block_stats(player_stats: PlayerStats) -> list:
    '''
    Collect the block stats from the player stats.
    '''
    player_block_stats = player_stats.block_stats
    if not isinstance(player_block_stats, BlockStats):
        raise ValueError("Player stats is not of type BlockStats")

    block_stats = []

    block_stats.append(player_block_stats.perfect_blocks)
    block_stats.append(player_block_stats.great_blocks)
    block_stats.append(player_block_stats.medium_blocks)
    block_stats.append(player_block_stats.poor_blocks)
    block_stats.append(player_block_stats.block_errors)
    block_stats.append(player_block_stats.total_blocks)
    block_stats.append(player_block_stats.block_average)

    return block_stats