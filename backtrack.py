from copy import deepcopy
import time
from table import Table
from utils import INF


class BackTrack:
    
    
    def __init__(self, table: Table) -> None:
        self.solved_table = None
        start = time.time()
        self.solve(table)
        self.time = time.time() - start
        
    
    def solve(self, table: Table):
        
        # LCV
        def tot_domains(value):
            new_table = deepcopy(table)
            if not new_table.cells[x][y].set_number_ec(value):
                return INF
            return -new_table.tot_cells_domain      
                  
        if not table.unfilled_cells:
            self.solved_table = table           
            return
        
        cell = table.pick_cell()
        x, y = cell.coordinates
        
        domain = cell.domain
        
        value_tot_domains = {
            value: tot_domains(value)
            for value in domain
            }
        
        # sort values according to LCV
        domain.sort(key= lambda x: value_tot_domains[x])
        domain = list(filter(
            lambda x: value_tot_domains[x] < INF,
            domain
        ))
        
        
        for value in domain:
            new_table = deepcopy(table)
            if not new_table.cells[x][y].set_number_ec(value):
                continue
            self.solve(new_table)
            if self.solved_table:
                return
        