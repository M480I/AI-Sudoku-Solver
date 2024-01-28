from UI import input_table
from table import Table
from copy import deepcopy


table = input_table()


# print(cell.connected_cells)

for i in range(3, 4):
    for j in range(3, 4):
        print(i, j, table.cells[i][j].connected_cells)
        
# print(len(table.unfilled_cells))
# for cell in table.unfilled_cells:
#     print(cell)
    
# best_cell = table.get_mcv()
# print(best_cell, best_cell.domain)
