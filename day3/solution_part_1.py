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


# # print grid
# for row in grid: 
#     print(row)


# the real shit
sum = 0
  
for row_index, row in enumerate(grid): 

    number = ""
    wrapper_cells = []

    for cell_index, cell in enumerate(row): 
        if cell.isdigit():
            number = number + cell
            
            # add top-left corner
            if row_index-1 >= 0 and cell_index-1 >= 0:
                wrapper_cells.extend(grid[row_index-1][cell_index-1])

            # add top
            if row_index-1 >= 0:
                wrapper_cells.extend(grid[row_index-1][cell_index])

            # add top-right corner
            if row_index-1 >= 0 and cell_index+1 < columns:
                wrapper_cells.extend(grid[row_index-1][cell_index+1])

            # add left
            if cell_index-1 >= 0:
                wrapper_cells.extend(grid[row_index][cell_index-1])

            # add right
            if cell_index+1 < columns:
                wrapper_cells.extend(grid[row_index][cell_index+1])

            # add bottom-left corner
            if row_index+1 < rows and cell_index+1 < columns:
                wrapper_cells.extend(grid[row_index+1][cell_index-1])

            # add bottom
            if row_index+1 < rows:
                wrapper_cells.extend(grid[row_index+1][cell_index])

            # add bottom-right corner
            if row_index+1 < rows and cell_index+1 < columns:
                wrapper_cells.extend(grid[row_index+1][cell_index+1])

            # the last character in the row is a digit so
            # check if it needs to be added to the sum
            if cell_index == columns-1:
                if not all(char.isdigit() or char=="." for char in wrapper_cells):
                    sum = sum + int(number)

        else:
            
            # check if it needs to be added to the sum
            if not number == "":
                if not all(char.isdigit() or char=="." for char in wrapper_cells):
                    sum = sum + int(number)

            # reset for next number
            number = ""
            wrapper_cells = []

    
input_file.close()
print("The sum is: ")
print(sum)