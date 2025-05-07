class FreeBallStats:
    def __init__(self) -> None:
        self.perfect_free_balls = 0
        self.great_free_balls = 0
        self.medium_free_balls = 0
        self.poor_free_balls = 0
        self.free_ball_errors = 0
        self.total_free_balls = 0
        self.free_ball_average = 0.0

    def set_perfect_free_balls(self, perfect_free_balls: int) -> None:
        '''
        Set the number of perfect free balls from the player free ball stats.
        '''
        self.perfect_free_balls = perfect_free_balls

    def set_great_free_balls(self, great_free_balls: int) -> None:
        '''
        Set the number of great free balls from the player free ball stats.
        '''
        self.great_free_balls = great_free_balls

    def set_medium_free_balls(self, medium_free_balls: int) -> None:
        '''
        Set the number of medium free balls from the player free ball stats.
        '''
        self.medium_free_balls = medium_free_balls

    def set_poor_free_balls(self, poor_free_balls: int) -> None:
        '''
        Set the number of poor free balls from the player free ball stats.
        '''
        self.poor_free_balls = poor_free_balls

    def set_free_ball_errors(self, free_ball_errors: int) -> None:
        '''
        Set the number of free ball errors from the player free ball stats.
        '''
        self.free_ball_errors = free_ball_errors

    def set_total_free_balls(self, total_free_balls: int) -> None:
        '''
        Set the total number of free balls from the player free ball stats.
        '''
        self.total_free_balls = total_free_balls

    def set_free_ball_average(self, free_ball_average: float) -> None:
        '''
        Set the average of the free ball stats.
        '''
        self.free_ball_average = free_ball_average  
    