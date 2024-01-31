from UI import input_table
from table import Table
from copy import deepcopy


table = input_table()


# print(cell.connected_cells)

for i in range(9):
    for j in range(9):
        cell = table.cells[i][j]      
        print(i, j, "\n", cell.domain, "\n", cell.rcs_domain)
        
print(table)

print(table.pick_cell())
  
        
# print(len(table.unfilled_cells))
# for cell in table.unfilled_cells:
#     print(cell)
    
# best_cell = table.get_mcv()
# print(best_cell, best_cell.domain)
