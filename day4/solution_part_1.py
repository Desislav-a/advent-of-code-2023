input_file = open('input.txt')

sum = 0

def get_game_id(line):
    return line.split(":")[0].split(" ")[1]

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

for line_index, line in enumerate(input_file):
    line = line.strip()

    game_id = get_game_id(line)
    
    winning_numbers = get_winning_numbers(line)

    scratched_numbers = get_scratched_numbers(line)

    common_numbers = list(set(winning_numbers).intersection(scratched_numbers))

    if common_numbers:
        sum = sum + (pow(2, len(common_numbers) - 1))
    
input_file.close()
print("The sum is: ")
print(sum)