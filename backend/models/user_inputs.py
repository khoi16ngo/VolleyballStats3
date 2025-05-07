from models.action import Action
from models.player import Player
from models.quality import Quality

class UserInputs:
    def __init__(self, players: list[Player], actions: list[Action], action_qualities: list[Quality], raw_data_file_paths: list[str]) -> None:
        self.players = players
        self.actions = actions
        self.action_qualities = action_qualities
        self.raw_data_file_paths = raw_data_file_paths

        self.assist_action = None
        self.attack_action = None
        self.block_action = None
        self.dig_action = None
        self.free_ball_action = None
        self.serve_action = None
        self.serve_receive_pass_action = None

        self.perfect_quality = None
        self.good_quality = None
        self.ok_quality = None
        self.poor_quality = None
        self.error_quality = None

    def set_assist_action(self, assist_action: Action) -> None:
        '''
        Set the assist action for the user inputs.
        '''
        self.assist_action = assist_action
    
    def set_attack_action(self, attack_action: Action) -> None:
        '''
        Set the attack action for the user inputs.
        '''
        self.attack_action = attack_action

    def set_block_action(self, block_action: Action) -> None:
        '''
        Set the block action for the user inputs.
        '''
        self.block_action = block_action

    def set_dig_action(self, dig_action: Action) -> None:
        '''
        Set the dig action for the user inputs.
        '''
        self.dig_action = dig_action

    def set_free_ball_action(self, free_ball_action: Action) -> None:
        '''
        Set the free ball action for the user inputs.
        '''
        self.free_ball_action = free_ball_action
    
    def set_serve_action(self, serve_action: Action) -> None:
        '''
        Set the serve action for the user inputs.
        '''
        self.serve_action = serve_action
    
    def set_serve_receive_pass_action(self, serve_receive_pass_action: Action) -> None:
        '''
        Set the serve receive pass action for the user inputs.
        '''
        self.serve_receive_pass_action = serve_receive_pass_action
    
    def set_perfect_quality(self, perfect_quality: Quality) -> None:
        '''
        Set the perfect quality for the user inputs.
        '''
        self.perfect_quality = perfect_quality
    
    def set_good_quality(self, good_quality: Quality) -> None:
        '''
        Set the good quality for the user inputs.
        '''
        self.good_quality = good_quality
    
    def set_ok_quality(self, ok_quality: Quality) -> None:
        '''
        Set the ok quality for the user inputs.
        '''
        self.ok_quality = ok_quality

    def set_poor_quality(self, poor_quality: Quality) -> None:
        '''
        Set the poor quality for the user inputs.
        '''
        self.poor_quality = poor_quality

    def set_error_quality(self, error_quality: Quality) -> None:
        '''
        Set the error quality for the user inputs.
        '''
        self.error_quality = error_quality
        