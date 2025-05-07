
from models.player import Player
from models.player_stats import PlayerStats
from models.stats.assist_stats import AssistStats
from models.stats.attack_stats import AttackStats
from models.stats.block_stats import BlockStats
from models.stats.dig_stats import DigStats
from models.stats.free_ball_stats import FreeBallStats
from models.stats.serve_receive_stats import ServeReceiveStats
from models.stats.serve_stats import ServeStats
from models.user_inputs import UserInputs
from services.stat_builders.raw_stat_builder import fetch_player_raw_attack_stats, fetch_player_raw_assist_stats, fetch_player_raw_block_stats, fetch_player_raw_dig_stats, fetch_player_raw_free_ball_stats, fetch_player_raw_serve_receive_stats, fetch_player_raw_serve_stats
from services.stat_calculators.assist_stat_calculator import calculate_player_assist_stats
from services.stat_calculators.attack_stat_calculator import calculate_player_attack_stats
from services.stat_calculators.block_stat_calculator import calculate_player_block_stats
from services.stat_calculators.dig_stat_calculator import calculate_player_dig_stats
from services.stat_calculators.free_ball_stat_calculator import calculate_player_free_ball_stats
from services.stat_calculators.serve_receive_stat_calculator import calculate_player_serve_receive_stats
from services.stat_calculators.serve_stat_calculator import calculate_player_serve_stats

def build_player_stats( user_inputs: UserInputs, player: Player, calculated_player_stats: dict) -> PlayerStats:
    '''
    Build the player stats from the calculated player stats.
    '''
    
    player_stats = PlayerStats(player, calculated_player_stats)

    assist_stats = _build_player_assist_stats(user_inputs, player.number, calculated_player_stats)
    player_stats.set_assist_stats(assist_stats)
    
    attack_stats = _build_player_attack_stats(user_inputs, player.number, calculated_player_stats)
    player_stats.set_attack_stats(attack_stats)

    block_stats = _build_player_block_stats(user_inputs, player.number, calculated_player_stats)
    player_stats.set_block_stats(block_stats)

    dig_stats = _build_player_dig_stats(user_inputs, player.number, calculated_player_stats)
    player_stats.set_dig_stats(dig_stats)
    
    free_ball_stats = _build_player_free_ball_stats(user_inputs, player.number, calculated_player_stats)
    player_stats.set_free_ball_stats(free_ball_stats)

    serve_receive_stats = _build_player_serve_receive_stats(user_inputs, player.number, calculated_player_stats)
    player_stats.set_serve_receive_stats(serve_receive_stats)

    serve_stats = _build_player_serve_stats(user_inputs, player.number, calculated_player_stats)
    player_stats.set_serve_stats(serve_stats)

    return player_stats

def _build_player_assist_stats(user_inputs: UserInputs, player_number: int, calculated_player_stats: dict) -> AssistStats: 
    '''
    Build the player assist stats from the calculated player stats.
    '''
    player_raw_assist_stats = fetch_player_raw_assist_stats(user_inputs, player_number, calculated_player_stats)
    return calculate_player_assist_stats(user_inputs, player_raw_assist_stats)

def _build_player_attack_stats(user_inputs: UserInputs, player_number: int, calculated_player_stats: dict) -> AttackStats:
    '''
    Build the player attack stats from the calculated player stats.
    '''
    player_raw_attack_stats = fetch_player_raw_attack_stats(user_inputs, player_number, calculated_player_stats)
    return calculate_player_attack_stats(user_inputs, player_raw_attack_stats)

def _build_player_block_stats(user_inputs: UserInputs, player_number: int, calculated_player_stats: dict) -> BlockStats:
    '''
    Build the player block stats from the calculated player stats.
    '''
    player_raw_block_stats = fetch_player_raw_block_stats(user_inputs, player_number, calculated_player_stats)
    return calculate_player_block_stats(user_inputs, player_raw_block_stats)
    
def _build_player_dig_stats(user_inputs: UserInputs, player_number: int, calculated_player_stats: dict) -> DigStats:
    '''
    Build the player dig stats from the calculated player stats.
    '''
    player_raw_dig_stats = fetch_player_raw_dig_stats(user_inputs, player_number, calculated_player_stats)
    return calculate_player_dig_stats(user_inputs, player_raw_dig_stats)

def _build_player_free_ball_stats(user_inputs: UserInputs, player_number: int, calculated_player_stats: dict) -> FreeBallStats:
    '''
    Build the player free ball stats from the calculated player stats.
    '''
    player_raw_free_ball_stats = fetch_player_raw_free_ball_stats(user_inputs, player_number, calculated_player_stats)
    return calculate_player_free_ball_stats(user_inputs, player_raw_free_ball_stats)

def _build_player_serve_receive_stats(user_inputs: UserInputs, player_number: int, calculated_player_stats: dict) -> ServeReceiveStats:
    '''
    Build the player serve receive stats from the calculated player stats.
    '''
    player_raw_serve_receive_stats = fetch_player_raw_serve_receive_stats(user_inputs, player_number, calculated_player_stats)
    return calculate_player_serve_receive_stats(user_inputs, player_raw_serve_receive_stats)
    
def _build_player_serve_stats(user_inputs: UserInputs, player_number: int, calculated_player_stats: dict) -> ServeStats:
    '''
    Build the player serve stats from the calculated player stats.
    '''
    player_raw_serve_stats = fetch_player_raw_serve_stats(user_inputs, player_number, calculated_player_stats)
    return calculate_player_serve_stats(user_inputs, player_raw_serve_stats)