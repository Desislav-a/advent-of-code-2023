input_file = open('input.txt')

sum = 0
blue_requirement = 14
red_requirement = 12
green_requirement = 13

def get_game_id(line):
    return line.split(":")[0].split(" ")[1]

def get_game_result(line):
    return line.split(":")[1].split(";")


for line in input_file:
    line = line.strip()

    game_id = get_game_id(line)
    
    game_result = get_game_result(line)

    all_cubes = []
    
    # make a list of all cubes
    for cube_set in game_result:
        all_cubes.extend(cube_set.split(","))

    
    requirement_met = True

    # check requirement against each cube based on colour
    for cubes in all_cubes:
        if "blue" in cubes:
            amount = cubes.strip().split(" ")[0]
            if int(amount) > blue_requirement:
                requirement_met = False
                break
        elif "red" in cubes:
            amount = cubes.strip().split(" ")[0]
            if int(amount) > red_requirement:
                requirement_met = False
                break
        elif "green" in cubes:
            amount = cubes.strip().split(" ")[0]
            if int(amount) > green_requirement:
                requirement_met = False
                break
        
    
    if requirement_met:
        sum = sum + int(game_id)


input_file.close()
print(sum)