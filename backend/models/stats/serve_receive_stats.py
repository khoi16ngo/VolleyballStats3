class ServeReceiveStats:
    def __init__(self) -> None:
        self.perfect_serve_receives = 0
        self.great_serve_receives = 0
        self.medium_serve_receives = 0
        self.poor_serve_receives = 0
        self.serve_receive_errors = 0
        self.total_serve_receives = 0
        self.in_system_percentage = 0.0
        self.out_of_system_percentage = 0.0
        self.serve_receive_average = 0.0

    def set_perfect_serve_receives(self, perfect_serve_receives: int) -> None:
        '''
        Set the number of perfect serve_receives from the player serve receive stats.
        '''
        self.perfect_serve_receives = perfect_serve_receives

    def set_great_serve_receives(self, great_serve_receives: int) -> None:
        '''
        Set the number of great serve_receives from the player serve receive stats.
        '''
        self.great_serve_receives = great_serve_receives

    def set_medium_serve_receives(self, medium_serve_receives: int) -> None:
        '''
        Set the number of medium serve_receives from the player serve receive stats.
        '''
        self.medium_serve_receives = medium_serve_receives

    def set_poor_serve_receives(self, poor_serve_receives: int) -> None:
        '''
        Set the number of poor serve_receives from the player serve receive stats.
        '''
        self.poor_serve_receives = poor_serve_receives

    def set_serve_receive_errors(self, serve_receive_errors: int) -> None:
        '''
        Set the number of serve errors from the player serve receive stats.
        '''
        self.serve_receive_errors = serve_receive_errors

    def set_total_serve_receives(self, total_serve_receives: int) -> None:
        '''
        Set the total number of serve_receives from the player serve receive stats.
        '''
        self.total_serve_receives = total_serve_receives

    def set_in_system_percentage(self, in_system_percentage: float) -> None:
        '''
        Set the in-system percentage of the serve receive stats.
        '''
        self.in_system_percentage = in_system_percentage

    def set_out_of_system_percentage(self, out_of_system_percentage: float) -> None:
        '''
        Set the out-of-system percentage of the serve receive stats.
        '''
        self.out_of_system_percentage = out_of_system_percentage

    def set_serve_receive_average(self, serve_receive_average: float) -> None:
        '''
        Set the average of the serve receive stats.
        '''
        self.serve_receive_average = serve_receive_average
        
        

    