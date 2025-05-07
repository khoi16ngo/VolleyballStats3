class ServeStats:
    def __init__(self) -> None:
        self.aces = 0
        self.great_serves = 0
        self.medium_serves = 0
        self.poor_serves = 0
        self.serve_errors = 0
        self.total_serves = 0
        self.opponent_out_of_system_percentage = 0.0
        self.opponent_in_system_percentage = 0.0
        self.serve_average = 0.0

    def set_aces(self, aces: int) -> None:
        '''
        Set the number of perfect serves from the player serve stats.
        '''
        self.aces = aces

    def set_great_serves(self, great_serves: int) -> None:
        '''
        Set the number of great serves from the player serve stats.
        '''
        self.great_serves = great_serves

    def set_medium_serves(self, medium_serves: int) -> None:
        '''
        Set the number of medium serves from the player serve stats.
        '''
        self.medium_serves = medium_serves

    def set_poor_serves(self, poor_serves: int) -> None:
        '''
        Set the number of poor serves from the player serve stats.
        '''
        self.poor_serves = poor_serves

    def set_serve_errors(self, serve_errors: int) -> None:
        '''
        Set the number of serve errors from the player serve stats.
        '''
        self.serve_errors = serve_errors

    def set_total_serves(self, total_serves: int) -> None:
        '''
        Set the total number of serves from the player serve stats.
        '''
        self.total_serves = total_serves

    def set_opponent_out_of_system_percentage(self, opponent_out_of_system_percentage: float) -> None:
        '''
        Set the opponent out-of-system percentage of the serve stats.
        '''
        self.opponent_out_of_system_percentage = opponent_out_of_system_percentage

    def set_opponent_in_system_percentage(self, opponent_in_system_percentage: float) -> None:
        '''
        Set the opponent in-system percentage of the serve stats.
        '''
        self.opponent_in_system_percentage = opponent_in_system_percentage

    def set_serve_average(self, serve_average: float) -> None:
        '''
        Set the average of the serve stats.
        '''
        self.serve_average = serve_average