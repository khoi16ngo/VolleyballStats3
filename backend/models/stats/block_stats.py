class BlockStats:
    def __init__(self) -> None:
        self.perfect_blocks = 0
        self.great_blocks = 0
        self.medium_blocks = 0
        self.poor_blocks = 0
        self.block_errors = 0
        self.total_blocks = 0
        self.block_average = 0.0

    def set_perfect_blocks(self, perfect_blocks: int) -> None:
        '''
        Set the number of perfect blocks from the player block stats.
        '''
        self.perfect_blocks = perfect_blocks

    def set_great_blocks(self, great_blocks: int) -> None:
        '''
        Set the number of great blocks from the player block stats.
        '''
        self.great_blocks = great_blocks
    
    def set_medium_blocks(self, medium_blocks: int) -> None:
        '''
        Set the number of medium blocks from the player block stats.
        '''
        self.medium_blocks = medium_blocks

    def set_poor_blocks(self, poor_blocks: int) -> None:
        '''
        Set the number of poor blocks from the player block stats.
        '''
        self.poor_blocks = poor_blocks

    def set_block_errors(self, block_errors: int) -> None:
        '''
        Set the number of block errors from the player block stats.
        '''
        self.block_errors = block_errors

    def set_total_blocks(self, total_blocks: int) -> None:
        '''
        Set the total number of blocks from the player block stats.
        '''
        self.total_blocks = total_blocks

    def set_block_average(self, block_average: float) -> None:
        '''
        Set the average of the block stats.
        '''
        self.block_average = block_average

        
