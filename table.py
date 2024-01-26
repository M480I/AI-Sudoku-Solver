class Cell:
    

    def __init__(self, row, column, table) -> None:
        self.row = row
        self.column = column
        self.table = table
        self.number = None
                
        self.coordinates = self.row, self.column
        
        self.cage = None
        
        
    @property
    def domain(self):
        row_d = set(self.table.row_domain[self.row])
        column_d = set(self.table.column_domain[self.column])
        square_d = \
            set(self.table.square_domain[self.row//3][self.column//3])
        
        return list(row_d & column_d & square_d)
        
        
        
    @property
    def connected_cells(self):
        return list(set(self.table.other_cells_all(self)
                    + self.cage.other_cells(self)))      
    
    
    def set_number(self, number):
        self.number = number
        
        self.table.row_domain[self.row].remove(number)
        self.table.column_domain[self.column].remove(number)
        self.table.square_domain[self.row//3][self.column//3].remove(number)
        
        self.table.unfilled_cells.remove(self)
        
    
    
    def __str__(self) -> str:
        return f"{self.number} in ({self.row}, {self.column})"
    
    
    def __repr__(self) -> str:
        return self.__str__()
    

class Table:
        
    
    def __init__(self) -> None:
        self.row_count = self.column_count = 9
        
        self.cells: list[Cell] = []
        self.unfilled_cells: list[Cell] = []
        
        _1_to_9 = [i for i in range(1, 10)]
        self.row_domain = [_1_to_9.copy() for _ in range(9)]
        self.column_domain = [_1_to_9.copy() for _ in range(9)]
        self.square_domain = [
            [
                _1_to_9.copy() for _ in range(3)
            ] for _ in range(3)
        ]
                
        self.make_cells()

        
    # make cells for board
    def make_cells(self):
        for x in range(self.row_count):
            row = []
            for y in range(self.column_count):
                cell = Cell(x, y, self)
                row.append(cell)
                self.unfilled_cells.append(cell)
            self.cells.append(row)


    def other_cells_column(self, cell):
        x, y = cell.coordinates
        res = []
        for i in range(self.row_count):
            if i == x:
                continue
            res.append(self.cells[i][y])
        return res
    

    def other_cells_row(self, cell):
        x, y = cell.coordinates
        res = []
        for i in range(self.column_count):
            if i == y:
                continue
            res.append(self.cells[x][i])
        return res

    def other_cells_square(self, cell):
        x, y = cell.coordinates
        x_sq = x - (x % 3)
        y_sq = y - (y % 3)
        res = []
        
        for i in range(x_sq, x_sq + 3):
            for j in range(y_sq, y_sq + 3):
                if i == x and j == y:
                    continue
                res.append(self.cells[i][j])
        return res
    
    
    def other_cells_all(self, cell):
        return list(set(self.other_cells_row(cell)
                    + self.other_cells_column(cell)
                    + self.other_cells_square(cell)
        ))
        
    # pick a cell to fill next 
    # according to most constrained variable 
    # and most constraining variable as a tie-breaker * toDo
    def pick_cell(self):
        self.unfilled_cells.sort(key=lambda x: len(x.domain))
        return self.unfilled_cells[0]


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
    
    
    def is_completed(self):
        for cell in self.cells:
            if cell.number is None:
                return False
        return True
    
    
    def is_satisfied(self):
        return self.is_completed() and self.sum == self.goal_sum
    
    
    def is_violated(self):
        return ((self.is_completed() and self.sum != self.goal_sum)
                or self.sum > self.goal_sum)
    
    
    def other_cells(self, cell):
        res = self.cells.copy()
        if cell not in res:
            raise RuntimeError
        res.remove(cell)
        return res
    