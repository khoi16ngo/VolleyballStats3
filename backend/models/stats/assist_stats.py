class AssistStats:
    def __init__(self) -> None:
        self.perfect_assists = 0
        self.great_assists = 0
        self.medium_assists = 0
        self.poor_assists = 0
        self.assist_errors = 0
        self.total_assists = 0
        self.assist_average = 0.0

    def set_perfect_assists(self, perfect_assists: int) -> None:
        '''
        Set the number of perfect assists from the player assist stats.
        '''
        self.perfect_assists = perfect_assists
    
    def set_great_assists(self, great_assists: int) -> None:
        '''
        Set the number of great assists from the player assist stats.
        '''
        self.great_assists = great_assists
    
    def set_medium_assists(self, medium_assists: int) -> None:
        '''
        Set the number of medium assists from the player assist stats.
        '''
        self.medium_assists = medium_assists

    def set_poor_assists(self, poor_assists: int) -> None:
        '''
        Set the number of poor assists from the player assist stats.
        '''
        self.poor_assists = poor_assists

    def set_assist_errors(self, assist_errors: int) -> None:
        '''
        Set the number of assist errors from the player assist stats.
        '''
        self.assist_errors = assist_errors

    def set_total_assists(self, total_assists: int) -> None:
        '''
        Set the total number of assists from the player assist stats.
        '''
        self.total_assists = total_assists

    def set_assist_average(self, assist_average: float) -> None:
        '''
        Set the average of the assist stats.
        '''     
        self.assist_average = assist_average
    