input_file = open('input.txt')
current_value = 0
string_value = 0


for line_index, line in enumerate(input_file):
    strings = line.strip().split(",")

    for string in strings:

        for char in string:
            string_value = ((string_value + ord(char)) * 17) % 256
        

        current_value = current_value + string_value
        string_value = 0


print(current_value)
input_file.close()

