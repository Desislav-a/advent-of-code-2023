input_file = open('input.txt')

# get number of lines
line_count = 0
for line in input_file:
    line_count = line_count + 1

input_file.close()
input_file = open('input.txt')

sum = 0

def get_game_id(line):
    return line.split(":")[0].split()[1]

def get_winning_numbers(line):
    winning_numbers = line.split(":")[1].split("|")[0]
    winning_numbers = winning_numbers.strip()
    winning_numbers_list = winning_numbers.split(" ")
    return winning_numbers_list

def get_scratched_numbers(line):
    scratched_numbers = line.split(":")[1].split("|")[1]
    scratched_numbers.strip()
    scratched_numbers_list = scratched_numbers.split()
    return scratched_numbers_list


# dictionary to keep track of cards and how many copies there are of them
cards_count = {}
keys = range(1, line_count + 1)

# start with one copy of each cards first
for i in keys:
    cards_count[i] = 1

# solution
for line_index, line in enumerate(input_file):
    line = line.strip()

    game_id = get_game_id(line)
    print("Game ID:" + game_id)
    
    winning_numbers = get_winning_numbers(line)
    scratched_numbers = get_scratched_numbers(line)

    common_numbers = list(set(winning_numbers).intersection(scratched_numbers))

    print("Copy next: " + str(len(common_numbers)) + " cards.")

    for copy in range(1, cards_count[int(game_id)] + 1):
        for i in range(1, len(common_numbers) + 1):
            cards_count[int(game_id) + i] = cards_count[int(game_id) + i] + 1


for value in cards_count.values():
    sum = sum + value

input_file.close()
print("The sum is: ")
print(sum)