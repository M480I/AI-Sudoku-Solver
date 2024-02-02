from arc import Arc
from utils import enforce_consistency


class Cell:
    

    def __init__(self, row, column, table) -> None:
        self.row = row
        self.column = column
        self.table = table
        self.number = None
        self.domain = list(range(1, 10))
                
        self.coordinates = self.row, self.column
        
        self.cage = None
        
        self.connected_cells = None
        self.connected_cells_rcs = None
        self.connected_cells_cage = None
        
        
    @property
    def connected_cells_unfilled_cnt(self):
        res = 0
        for cell in self.connected_cells:
            res += cell.number is None
        return res
        
        
    @property
    def rcs_domain(self):
        row_d = set(self.table.row_domain[self.row])
        column_d = set(self.table.column_domain[self.column])
        square_d = \
            set(self.table.square_domain[self.row//3][self.column//3])
        
        return list(row_d & column_d & square_d)
        
    
    def set_connected_cells_rcs(self):
        self.connected_cells_rcs = \
            self.table.other_cells_rcs(self)
    
    
    def set_connected_cells_cage(self):
        self.connected_cells_cage = \
            self.cage.other_cells_cage(self)
            
        self.set_connected_cells()
    
    
    def set_connected_cells(self):
        self.connected_cells = \
            list(set(self.connected_cells_rcs
                     + self.connected_cells_cage
                     ))

    
    def set_number(self, number):
        self.number = number
        self.domain.clear()
        self.domain.append(number)
        self.table.row_domain[self.row].remove(number)
        self.table.column_domain[self.column].remove(number)
        self.table.square_domain[self.row//3][self.column//3].remove(number)
        self.table.unfilled_cells.remove(self)
    
    # put a number in cell then perform forward-checking
    # and enforce consistency on arcs
    def set_number_ec(self, number) -> bool:
        
        self.set_number(number)
                
        arcs = []
        
        for cell in self.connected_cells:
            if cell.number is not None:
                continue
            arc = Arc(first=cell,
                    second=self,
                    )
            arcs.append(arc)
            
        return enforce_consistency(arcs)    
    
    
    def __str__(self) -> str:
        return f"{self.number} in ({self.row}, {self.column})"
    
    
    def __repr__(self) -> str:
        return self.__str__()
