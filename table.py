class Cell:
    

    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column
                
        self.coordinates = self.row, self.column
        
        self.domain = []
        self.cage = None
    
    
    @property
    def filled(self):
        return len(self.domain) == 1        
        
        
    @property
    def number(self):
        if self.filled:
            return self.domain[0]
        return None
    
    
    def __str__(self) -> str:
        return f"{self.number} in ({self.row}, {self.column})"
    
    
    def __repr__(self) -> str:
        return self.__str__()
    

class Table:
        
    
    def __init__(self) -> None:
        self.row_count = self.column_count = 9
        
        self.cells: list[Cell] = []
        
        self.make_cells()

        
    # make cells for board>
    def make_cells(self):
        for x in range(self.row_count):
            row = []
            for y in range(self.column_count):
                row.append(Cell(x, y))
            self.cells.append(row)    
                
    
    def __str__(self) -> str:
        
        res = ""
        sep1 = " " + self.column_count*"+-------"  + "+\n"
        sep2 = " |   "
        sep3 = "  "
        sep4 = " " + self.column_count*"|       " + "|\n"
        
        for i in range(self.row_count):
            res += sep1
            res += sep4
            for j in range(self.column_count):
                if self.cells[i][j].number is None:
                    number = " "
                else:
                    number = self.cells[i][j].number
                res += sep2 + str(number) + sep3
            res += " |\n"
            res += sep4
        res += sep1
        
        return res
    
    
    def __repr__(self) -> str:
        return self.__str__()


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
    
    
    def is_complete(self):
        for cell in self.cells:
            if cell.number is None:
                return False
        return True
    
    
    def is_met(self):
        return self.is_complete and self.sum == self.goal_sum
    
    
    def is_violated(self):
        return self.is_complete and self.sum != self.goal_sum