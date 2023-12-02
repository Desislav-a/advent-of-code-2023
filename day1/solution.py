input_file = open('input.txt')

sum = 0

for line in input_file:
    line = line.strip()
    first_digit = ""
    second_digit = ""
    
    # get first digit
    for character in line:
        if character.isdigit():
            first_digit = character
            break

    # get second digit
    for character in reversed(line):
        if character.isdigit():
            second_digit = character
            break

    sum = sum + int(first_digit + second_digit)

input_file.close()
print(sum)