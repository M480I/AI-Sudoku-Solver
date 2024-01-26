from UI import input_table
from table import Table

table = input_table()
print(table)
x, y = 4, 6

for i in range(9):
    for j in range(9):
        print(i, j, table.cells[i][j].domain)
        
print(len(table.unfilled_cells))
for cell in table.unfilled_cells:
    print(cell)
    
best_cell = table.get_mcv()
print(best_cell, best_cell.domain)
