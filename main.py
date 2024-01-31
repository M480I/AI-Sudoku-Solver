from UI import input_table
from table import Table
from copy import deepcopy


table = input_table()


# print(cell.connected_cells)

for i in range(9):
    for j in range(9):
        cell = table.cells[i][j]      
        print(i+1, j+1, "\n", cell.domain, "\n")
        
print(table)

for cell in table.pick_cell():
    print(cell, cell.connected_cells_unfilled_cnt, sep="\n")
  
        
# print(len(table.unfilled_cells))
# for cell in table.unfilled_cells:
#     print(cell)
    
# best_cell = table.get_mcv()
# print(best_cell, best_cell.domain)
