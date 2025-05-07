class DigStats:
    def __init__(self) -> None:
        self.perfect_digs = 0
        self.great_digs = 0
        self.medium_digs = 0
        self.poor_digs = 0
        self.dig_errors = 0
        self.total_digs = 0
        self.dig_average = 0.0

    def set_perfect_digs(self, perfect_digs: int) -> None:
        '''
        Set the number of perfect digs from the player dig stats.
        '''
        self.perfect_digs = perfect_digs

    def set_great_digs(self, great_digs: int) -> None:
        '''
        Set the number of great digs from the player dig stats.
        '''
        self.great_digs = great_digs
    
    def set_medium_digs(self, medium_digs: int) -> None:
        '''
        Set the number of medium digs from the player dig stats.
        '''
        self.medium_digs = medium_digs

    def set_poor_digs(self, poor_digs: int) -> None:
        '''
        Set the number of poor digs from the player dig stats.
        '''
        self.poor_digs = poor_digs

    def set_dig_errors(self, dig_errors: int) -> None:
        '''
        Set the number of dig errors from the player dig stats.
        '''
        self.dig_errors = dig_errors

    def set_total_digs(self, total_digs: int) -> None:
        '''
        Set the total number of digs from the player dig stats.
        '''
        self.total_digs = total_digs

    def set_dig_average(self, dig_average: float) -> None:
        '''
        Set the average of the dig stats.
        '''
        self.dig_average = dig_average

    