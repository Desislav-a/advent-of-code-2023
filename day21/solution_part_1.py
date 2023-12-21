from collections import deque as queue

input_file = open('input.txt')

# get rows and columns number
rows = 0
columns = 0
for line in input_file:
    rows = rows + 1
    columns = len(line)

input_file.close()


# make the grid 
grid = [[0 for x in range(columns)] for y in range(rows)] 

# populate the grid 
input_file = open('input.txt')

for line_index, line in enumerate(input_file):
    line = line.strip()

    for char_index, char in enumerate(line):
        grid[line_index][char_index] = char


# print grid
for row in grid: 
    print(row)


# find the starting point
starting_row = 0
starting_column = 0

for row_index, row in enumerate(grid): 
    for cell_index, cell in enumerate(row): 

        if cell == "S":
            starting_row = row_index
            starting_column = cell_index



dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]
 
# Function to check if a cell
# is be visited or not
def isValid(row, col):
   
    # If cell lies out of bounds
    if (row < 0 or col < 0 or row >= rows or col >= columns):
        return False

    if grid[row][col] == "#":
        return False
 
    # Otherwise
    return True

# breadth first seach changed to do only 64 steps
def BFS(grid, row, col):
   

    parents = queue()
    children = queue()

    parents.append(( row, col ))


    steps = 64

    while steps > 0:

        if len(parents) == 0:
            print("Steps:" + str(steps))
            parents = children
            children = queue()
            steps = steps - 1

        
        cell = parents.popleft()
        x = cell[0]
        y = cell[1]
 
 
        # Go to the adjacent cells
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]

            if (isValid(adjx, adjy)):
                children.append((adjx, adjy))
        
        children = queue(set(list(children)))

    # print(parents) & account for the popped child
    print(len(parents) + 1)



BFS(grid, starting_row, starting_column)