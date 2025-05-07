from models.quality import Quality
from models.stats.block_stats import BlockStats
from models.user_inputs import UserInputs

def calculate_player_block_stats(user_inputs: UserInputs, player_raw_block_stats: dict) -> BlockStats:
    '''
    Calculate the player block stats from the user inputs and the player raw block stats.
    Returns a BlockStats object with the calculated stats.
    '''
    player_block_stats = BlockStats()
    player_block_stats.set_perfect_blocks(_get_perfect_blocks(user_inputs, player_raw_block_stats))
    player_block_stats.set_great_blocks(_get_great_blocks(user_inputs, player_raw_block_stats))  
    player_block_stats.set_medium_blocks(_get_medium_blocks(user_inputs, player_raw_block_stats))   
    player_block_stats.set_poor_blocks(_get_poor_blocks(user_inputs, player_raw_block_stats))
    player_block_stats.set_block_errors(_get_block_errors(user_inputs, player_raw_block_stats))
    player_block_stats.set_total_blocks(_get_total_blocks(user_inputs, player_raw_block_stats))
    player_block_stats.set_block_average(_get_block_average(user_inputs, player_raw_block_stats))
    return player_block_stats

def _get_perfect_blocks(user_inputs: UserInputs, player_block_raw_stats: dict) -> int:
    '''
    Get the number of perfect blocks from the player block stats.
    '''
    return player_block_raw_stats[user_inputs.perfect_quality.value]

def _get_great_blocks(user_inputs: UserInputs, player_block_raw_stats: dict) -> int:
    '''
    Get the number of great blocks from the player block stats.
    '''
    return player_block_raw_stats[user_inputs.good_quality.value]

def _get_medium_blocks(user_inputs: UserInputs, player_block_raw_stats: dict) -> int:
    '''
    Get the number of medium blocks from the player block stats.
    '''
    return player_block_raw_stats[user_inputs.ok_quality.value]

def _get_poor_blocks(user_inputs: UserInputs, player_block_raw_stats: dict) -> int:
    '''
    Get the number of poor blocks from the player block stats.
    '''
    return player_block_raw_stats[user_inputs.poor_quality.value]

def _get_block_errors(user_inputs: UserInputs, player_block_raw_stats: dict) -> int:
    '''
    Get the number of block errors from the player block stats.
    '''
    return player_block_raw_stats[user_inputs.error_quality.value]

def _get_total_blocks(user_inputs: UserInputs, player_raw_block_stats: dict) -> int:
    '''
    Get the total number of blocks from the player block stats.
    '''
    perfect_blocks = _get_perfect_blocks(user_inputs, player_raw_block_stats)    
    great_blocks = _get_great_blocks(user_inputs, player_raw_block_stats)
    medium_blocks = _get_medium_blocks(user_inputs, player_raw_block_stats)
    poor_blocks = _get_poor_blocks(user_inputs, player_raw_block_stats)
    block_errors = _get_block_errors(user_inputs, player_raw_block_stats)

    return perfect_blocks + great_blocks + medium_blocks + poor_blocks + block_errors

def _get_block_average(user_inputs: UserInputs, player_raw_block_stats: dict) -> float:
    '''
    Get the average of the block stats.
    The average is calculated by weighting the blocks with the following weights:
    - Perfect blocks: 4
    - Great blocks: 3
    - Good blocks: 2
    - Poor blocks: 1
    - Block errors: 0.5
    '''
    total_blocks = _get_total_blocks(user_inputs, player_raw_block_stats)
    if total_blocks == 0:
        return 0.0
    
    total_weighted_blocks = (_get_perfect_blocks(user_inputs, player_raw_block_stats) * 4) + (_get_great_blocks(user_inputs, player_raw_block_stats) * 3) + (_get_medium_blocks(user_inputs, player_raw_block_stats) * 2) + (_get_poor_blocks(user_inputs, player_raw_block_stats) * 1) + (_get_block_errors(user_inputs, player_raw_block_stats) * 0.5)
    return total_weighted_blocks / total_blocks


