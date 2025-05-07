from models.player import Player
from models.stats.assist_stats import AssistStats
from models.stats.attack_stats import AttackStats
from models.stats.block_stats import BlockStats
from models.stats.dig_stats import DigStats
from models.stats.free_ball_stats import FreeBallStats
from models.stats.serve_receive_stats import ServeReceiveStats
from models.stats.serve_stats import ServeStats

class PlayerStats:
    def __init__(self, player: Player, player_calculated_stats: dict) -> None:
        self.player_name = player.name
        self.player_number = player.number
        self.player_calculated_stats = player_calculated_stats

        self.assist_stats = None
        self.attack_stats = None
        self.block_stats = None
        self.dig_stats = None
        self.free_ball_stats = None
        self.serve_receive_stats = None
        self.serve_stats = None

    def set_assist_stats(self, assist_stats: AssistStats) -> None:
        '''
        Set the assist stats for the player.
        '''
        self.assist_stats = assist_stats

    def set_attack_stats(self, attack_stats: AttackStats) -> None:
        '''
        Set the attack stats for the player.
        '''
        self.attack_stats = attack_stats

    def set_block_stats(self, block_stats: BlockStats) -> None:
        '''
        Set the block stats for the player.
        '''
        self.block_stats = block_stats

    def set_dig_stats(self, dig_stats: DigStats) -> None:
        '''
        Set the dig stats for the player.
        '''
        self.dig_stats = dig_stats

    def set_free_ball_stats(self, free_ball_stats: FreeBallStats) -> None:
        '''
        Set the free ball stats for the player.
        '''
        self.free_ball_stats = free_ball_stats

    def set_serve_receive_stats(self, serve_receive_stats: ServeReceiveStats) -> None:
        '''
        Set the serve receive stats for the player.
        '''
        self.serve_receive_stats = serve_receive_stats
    
    def set_serve_stats(self, serve_stats: ServeStats) -> None:
        '''
        Set the serve stats for the player.
        '''
        self.serve_stats = serve_stats
    