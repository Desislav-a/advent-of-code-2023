

input_file = open("input.txt")

steps = "LRRRLRRLRLRRRLRLLLLRRRLRLRRLRLRLRRLRRRLRRLRRRLRLLLRRLRRLRRLRRLRRLLLLLRLRLRRRLRLLRRLRLRRRLRRLRRRLLLRRLRRLRRLRRRLRLRLRRLLRRRLRRLRRRLRRRLRRRLRLRRLRRLRRLRRRLRLRRLRRLLRRRLRRLRRLRRRLRLRLRRLLRRRLLRRLRRRLRRRLRLRRLLRRRLRLRRLLRRLRLRRRLRLRRRLRRLRRLRRLRRRLRRRLRLLRRLRRLLRRLRRRLRRLRLRLRRRLLLRRLRLRRLRRLRLRLLRLRRLRLRLRRRR"

# steps = "LLR"

def get_directions():
    directions = [] 

    # make list of directions
    for line_index, line in enumerate(input_file):
        line = line.strip()
        node = line.split("=")[0].strip()
        next_node_left  = line.split("=")[1].split(",")[0][2:].strip()
        next_node_right = line.split("=")[1].split(",")[1][:-1].strip()
        directions.append([node, next_node_left, next_node_right])

    input_file.close()

    return directions


directions = get_directions()

current_node = "AAA"
steps_made = 0
end_reached = False

print(steps)

while not end_reached:

    for step in steps:

        if not end_reached:
            for direction in directions:

                if direction[0] == current_node:
                    print(step)
                    print(direction)
                    print()
                    if direction[0] == "ZZZ": 
                        end_reached = True  
                        break  

                    if step == "L":
                        current_node = direction[1]
                        steps_made = steps_made + 1
                    elif step == "R":
                        current_node = direction[2]
                        steps_made = steps_made + 1


print("The sum is: ")
print(steps_made)