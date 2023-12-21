from collections import deque

class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()



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


# # print grid
# for row in grid: 
#     print(row)

# tild the board and shift the rocks
for column_index in range(columns):

    last_seen_free_space = -1
    queue = Queue()

    for row_index, row in enumerate(grid): 

        if grid[row_index][column_index] == "O":
            if not len(queue) == 0:
                grid[row_index][column_index] = "."
                grid[queue.dequeue()][column_index] = "O"
                queue.enqueue(row_index)

        elif grid[row_index][column_index] == ".":
            queue.enqueue(row_index)

        
        elif grid[row_index][column_index] == "#":
            queue = Queue()
        
     
# # print grid
# for row in grid: 
#     print(row)

total_weight = 0

# calculate the weight of the shifted rocks
for row_index, row in enumerate(grid): 
    for cell_index, cell in enumerate(row): 

        if cell == "O":
            total_weight = total_weight +  rows - row_index


print(total_weight)