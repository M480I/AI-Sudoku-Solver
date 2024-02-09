from cell import Cell
from utils import INF
from copy import deepcopy, copy
    

class Table:
        
    
    def __init__(self) -> None:
        self.row_count = self.column_count = 9
        
        self.cells: list[list[Cell]] = []
        self.unfilled_cells: list[tuple[int, int]] = []
        
        _1_to_9 = list(range(1,10))
        self.row_domain = [_1_to_9.copy() for _ in range(9)]
        self.column_domain = [_1_to_9.copy() for _ in range(9)]
        self.square_domain = [
            [
                _1_to_9.copy() for _ in range(3)
            ] for _ in range(3)
        ]
                
        self.make_cells()
        
        self.no_solution = False
        self.cages_set = False
        
        
    # def is_valid(self) -> bool:
    #     for x in range(self.row_count):
    #         for y in range(self.column_count):
    #             cell = self.cells[x][y]
    #             if cell.cage.sum != cell.cage.goal_sum:
    #                 return False
    #     return True

        
    # make cells for board
    def make_cells(self):
        for x in range(self.row_count):
            row = []
            for y in range(self.column_count):
                cell = Cell(x, y, self)
                row.append(cell)
                self.unfilled_cells.append(cell.coordinates)
            self.cells.append(row)
            
        for x in range(self.row_count):
            for y in range(self.column_count):
                cell = self.cells[x][y]
                cell.set_connected_cells_rcs()


    def other_cells_row(self, cell):
        x, y = cell.coordinates
        res = []
        for i in range(self.column_count):
            if i == y:
                continue
            res.append(self.cells[x][i])
        return res
    
    
    def other_cells_column(self, cell):
        x, y = cell.coordinates
        res = []
        for i in range(self.row_count):
            if i == x:
                continue
            res.append(self.cells[i][y])
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
    
    
    def other_cells_rcs(self, cell):
        return list(set(self.other_cells_row(cell)
                    + self.other_cells_column(cell)
                    + self.other_cells_square(cell)
        ))
        
    
    @property
    def tot_cells_domain(self):
        res = 0
        unfilled_cells = self.unfilled_cells
        for x, y in unfilled_cells:
            cell = self.cells[x][y]
            res += len(cell.domain)
        res += (self.row_count*self.column_count
                - len(unfilled_cells))
        return res
    
        
    # pick a cell to fill next 
    # according to most constrained variable 
    # and most constraining variable as a tie-breaker
    def pick_cell(self):
        bests = [self.cells[x][y] for x, y in self.unfilled_cells]
        
        bests.sort(
            key=lambda x: len(x.domain) if len(x.domain) > 1 else INF,
            )
        
        smallest_domain_len = len(bests[0].domain)
        bests = list(filter(
            lambda x: len(x.domain) == smallest_domain_len,
            bests
            ))
        
        bests.sort(
            key=lambda x: 
                -(x.connected_cells_unfilled_cnt),
        )
        
        return bests[0]


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
    
    
    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}
            
        new_table = copy(self)
        
        new_table.cells = deepcopy(self.cells, memo)
        new_table.unfilled_cells = deepcopy(self.unfilled_cells, memo)
        new_table.row_domain = deepcopy(self.row_domain, memo)
        new_table.column_domain = deepcopy(self.column_domain, memo)
        new_table.square_domain = deepcopy(self.square_domain, memo)
        
        return new_table
