from table import Cell


class Arc:

    
    def __init__(self, first: Cell, second: Cell) -> None:
        self.first = first
        self.second = second
        
        self.domain_changed = None
    
    
    def enforce_consistency(self):
        pass
        # toDo
                