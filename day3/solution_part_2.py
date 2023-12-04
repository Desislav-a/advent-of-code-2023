input_file = open('input.txt')

# get rows and columns number
rows = 0
for line in input_file:
    rows = rows + 1
    columns = len(line)


# print(rows)
# print(columns)

# make the grid 
grid = [[0 for x in range(columns)] for y in range(rows)] 

# populate the grid 
input_file.close()
input_file = open('input.txt')

for line_index, line in enumerate(input_file):
    line = line.strip()

    for char_index, char in enumerate(line):
        grid[line_index][char_index] = char


# print grid
for row in grid: 
    print(row)


# the real shit
sum = 0
  
for row_index, row in enumerate(grid): 



    for cell_index, cell in enumerate(row): 
        
    
input_file.close()
print("The sum is: ")
print(sum)