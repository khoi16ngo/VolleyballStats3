class AttackStats:
    def __init__(self) -> None:
        self.kills = 0
        self.great_attacks = 0
        self.medium_attacks = 0
        self.poor_attacks = 0
        self.attack_errors = 0
        self.total_attacks = 0
        self.hitting_percentage = 0.0
        self.kill_percentage = 0.0
        self.hitting_average = 0.0

    def set_kills(self, kills: int) -> None:
        '''
        Set the number of kills from the player attack stats.
        '''
        self.kills = kills
    
    def set_great_attacks(self, great_attacks: int) -> None:
        '''
        Set the number of great attacks from the player attack stats.
        '''
        self.great_attacks = great_attacks

    def set_medium_attacks(self, medium_attacks: int) -> None:
        '''
        Set the number of medium attacks from the player attack stats.
        '''
        self.medium_attacks = medium_attacks

    def set_poor_attacks(self, poor_attacks: int) -> None:
        '''
        Set the number of poor attacks from the player attack stats.
        '''
        self.poor_attacks = poor_attacks

    def set_attack_errors(self, attack_errors: int) -> None:
        '''
        Set the number of attack errors from the player attack stats.
        '''
        self.attack_errors = attack_errors

    def set_total_attacks(self, total_attacks: int) -> None:
        '''
        Set the total number of attacks from the player attack stats.
        '''
        self.total_attacks = total_attacks

    def set_hitting_percentage(self, hitting_percentage: float) -> None:
        '''
        Set the hitting percentage of the player.
        '''
        self.hitting_percentage = hitting_percentage    

    def set_kill_percentage(self, kill_percentage: float) -> None:
        '''
        Set the kill percentage of the player.
        '''
        self.kill_percentage = kill_percentage
    
    def set_hitting_average(self, hitting_average: float) -> None:
        '''
        Set the hitting average of the player.
        '''
        self.hitting_average = hitting_average