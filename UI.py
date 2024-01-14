from table import Table, Cage


def input_table():
    table = Table()
    for i in range(9):
        row = list(map(int, input().split(" ")))
        for j in range(9):
            if row[j]:
                table.cells[i][j].domain.append(row[j])
                
    cage_count = int(input())
    
    for _ in range(cage_count):
        
        line = input().split(" ")
        print(line)
        sum = int(line[-1])
        cells = []
       
        for cell_cord in line[:-2]:
            
            cell_cord = list(map(int, cell_cord))
            x, y = cell_cord
            cell = table.cells[x][y]
            cells.append(cell)
           
        cage = Cage(cells=cells, goal_sum=sum)
        
        for cell in cells:
            cell.cage = cage
    
    return table            
    