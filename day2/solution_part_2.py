input_file = open('input.txt')

sum = 0

def get_game_id(line):
    game_id = line.split(":")[0].split(" ")[1]
    return game_id

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

    max_blue_seen = 0
    max_red_seen = 0 
    max_green_seen = 0
    
    # go through the cubes and get the max seen for each colour
    for cubes in all_cubes:
        if "blue" in cubes:
            amount = cubes.strip().split(" ")[0]
            max_blue_seen = max(max_blue_seen, int(amount))
            
        elif "red" in cubes:
            amount = cubes.strip().split(" ")[0]
            max_red_seen = max(max_red_seen, int(amount))

        elif "green" in cubes:
            amount = cubes.strip().split(" ")[0]
            max_green_seen = max(max_green_seen, int(amount))
           
    
    sum = sum + int(max_blue_seen*max_red_seen*max_green_seen)


input_file.close()
print(sum)