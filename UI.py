from table import Table
from cage import Cage
from queue import Queue
from arc import Arc
from backtrack import BackTrack
from utils import enforce_consistency


def input_table():
    table = Table()
    
    inpt_table = []
    for i in range(9):
        row = list(map(int, input().split(" ")))
        inpt_table.append(row)
    
    # make cages    
    cage_count = int(input())
    
    for _ in range(cage_count):
        
        line = input().split(" ")
        sum = int(line[-1])
        cells = []
       
        for cell_cord in line[:-2]:
            
            cell_cord = list(map(int, cell_cord))
            x, y = cell_cord
            cell = table.cells[x-1][y-1]
            cells.append(cell)
           
        cage = Cage(cells=cells, goal_sum=sum)
        
        for cell in cells:
            cell.cage = cage
            cell.set_connected_cells_cage()
            
    
    # pre-process for forward-checking 
    arcs = Queue()       
    for i in range(9):
        for j in range(9):
            cell = table.cells[i][j]
            for adj_cell in cell.connected_cells_cage:
                arc = Arc(first=cell, second=adj_cell)
                arcs.put(arc)
    enforce_consistency(arcs)
    
    
                
    # set initial numbers
    no_solution = False
    for i in range(9):
        for j in range(9):
            if inpt_table[i][j] and table.cells[i][j].number is None:
                if not table.cells[i][j].set_number_ec(inpt_table[i][j]):
                    no_solution = True
                    break
                    
    if no_solution:
        print("no solution.")
    

    return table


def solve_table(table):
    bt = BackTrack(table)           
    