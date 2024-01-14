from queue import PriorityQueue


class BackTrack:
    
    
    def __init__(self, board) -> None:
        self.board = board
        
        self.to_fix = PriorityQueue()
