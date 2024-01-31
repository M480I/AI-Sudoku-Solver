class Cage:
    
    
    def __init__(self, cells, goal_sum) -> None:
        self.cells = cells
        self.goal_sum = goal_sum
        
    
    @property
    def sum(self):
        res = 0
        for cell in self.cells:
            number = cell.number
            if number is not None:
                res += number
        return res
    
    
    # not filled count
    @property
    def n_filled_cnt(self):
        res = 0
        for cell in self.cells:
            if cell.number is None:
                res += 1
        return res
    
    
    def other_cells_cage(self, cell):
        res = self.cells.copy()
        if cell not in res:
            raise RuntimeError
        res.remove(cell)
        return res    
    
    
    def is_valid_arc(self, first, first_value, second, second_value):
        
        sum = self.sum
        completed = len(self.cells) - self.n_filled_cnt
        
        if first not in self.cells or second not in self.cells:
            raise RuntimeError
        if first.number is None:
            completed += 1
            sum += first_value
        if second.number is None:
            completed += 1
            sum += second_value
            
        if sum == self.goal_sum and completed == len(self.cells):
            return True
        if sum < self.goal_sum and completed < len(self.cells):
            return True
        return False
    