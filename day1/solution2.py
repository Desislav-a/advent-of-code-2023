input_file = open('input.txt')

sum = 0

for line in input_file:
    line = line.strip()
    first_digit = ""
    second_digit = ""

    # repalce string digits with number digits
    string_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    current_chars = ""
    first_digit_found = False

    # get first digit
    for character in line:
        if not first_digit_found:
            if character.isdigit():
                first_digit = character
                break
            else: 
                current_chars = current_chars + character
                for index, digit in enumerate(string_digits):
                        if digit in current_chars:
                            first_digit = index + 1
                            first_digit_found = True
                            break

    # get second digit
    current_chars = ""
    second_digit_found = False

    for character in reversed(line):
        if not second_digit_found:
            if character.isdigit():
                second_digit = character
                break
            else: 
                current_chars = current_chars + character
                current_chars
                for index, digit in enumerate(string_digits):
                        if digit in current_chars[::-1]:
                            second_digit_found = True
                            second_digit = index + 1
                            break


    print(int(str(first_digit) + str(second_digit)))


    sum = sum + int(str(first_digit) + str(second_digit))

input_file.close()
print(sum)