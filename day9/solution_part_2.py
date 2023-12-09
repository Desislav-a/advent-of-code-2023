input_file = open("input.txt")

next_elements = []

# get all the differences down to all 0s (recursive)
def get_differences(elements):

    if all(x == 0 for x in elements):
        return
    
    differences_between_elements = []

    for element_index, element in enumerate(elements[:-1]):
        differences_between_elements.append(elements[element_index + 1] - element)

    get_differences(differences_between_elements)
    next_elements.append(differences_between_elements[len(differences_between_elements)-1])


final_elements = []

for line_index, line in enumerate(input_file):
    elements = line.strip().split()
    
    for element_index, element in enumerate(elements):
        elements[element_index] = int(element)


    elements.reverse()

    get_differences(elements)

    final_element = 0

    for element_index, element in enumerate(next_elements[:-1]):
        final_element = final_element + next_elements[element_index + 1]


    final_elements.append(final_element + elements[len(elements) - 1])
    next_elements = []


print(sum(final_elements))
