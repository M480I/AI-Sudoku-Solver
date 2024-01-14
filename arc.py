from table import Cell


class Arc:

    
    def __init__(self, first: Cell, second: Cell) -> None:
        self.first = first
        self.second = second
        
        self.domain_changed = None
    
    
    def enforce_consistency(self):
        for f_value in self.first.domain:
            
            is_valid = False
            
            if len(self.second.domain) > 1:
                is_valid = True
            else:
                is_valid = self.second.domain[0] != f_value
                
            if not is_valid:
                self.domain_changed = True
                self.first.domain.remove(f_value)
                