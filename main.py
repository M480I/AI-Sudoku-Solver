from UI import input_table
from table import Table

table = input_table()
print(table)

for i in range(9):
    for j in range(9):
        cell = table.cells[i][j]
        print(cell.cage.goal_sum)

