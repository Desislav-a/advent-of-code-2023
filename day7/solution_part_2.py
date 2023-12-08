sum=0

# extract input into list 
def get_cards():
    input_file = open('input.txt')
    card_list = []

    for line_index, line in enumerate(input_file):
        line = line.strip().split()
        card_list.append([line[0], line[1]])

    input_file.close()
    return card_list

cards = get_cards()

# 7 Five of a kind - 5 of the same - AAAAA
# 6 Four of a kind - 4 of the same - AAAAB
# 5 Full house - 3 of the same & 2 of the same - AAABB
# 4 Three of a kind - 3 of the same & 2 different - AAABC
# 3 Two pair - 2 pairs - AABBC
# 2 One pair - 1 pair & 3 different - AABCD
# 1 High card - all different - ABCDE


def get_card_value(card):
    # print(card)

    # check for high card
    if len(set(card)) == len(card):
        # print("High card - all are diffrent!")
        return 1

    # check for five of a kind
    if len(set(card)) == 1:
        # print("Five of a kind - they are all the same!")
        return 7

    # check for four of a kind OR fullhouse
    if len(set(card)) == 2:
        if card.count(card[0]) == 4 or card.count(card[0]) == 1:
            # print("Four of a kind!")
            return 6
        else:
            # print("Full house")
            return 5

    # check for three of a kind OR two pair
    if len(set(card)) == 3:
        if card.count(card[0]) == 3:
            # print("Three of a kind!")
            return 4
        elif card.count(card[0]) == 2:
            # print("Two pair")
            return 3
        elif card.count(card[0]) == 1:
            if card.count(card[1]) == 3 or card.count(card[1]) == 1:
                # print("Three of a kind!")
                return 4
            elif card.count(card[1]) == 2:
                # print("Two pair")
                return 3

    # check for one pair
    if len(set(card)) == 4:
        # print("One pair")
        return 2


# this makes me cry but i understand it
def get_card_value_with_J(card):

    if not "J" in card:
        return get_card_value(card)

    if get_card_value(card) == 1:
        return 2

    if get_card_value(card) == 2:
        if card.count("J") == 2:
            return 4
        return 4

    if get_card_value(card) == 3:
        if card.count("J") == 2:
            return 6
        return 5

    if get_card_value(card) == 4:
        return 6

    if get_card_value(card) == 5:
        if len(set(card)) == 2:
            return 7
        return 6

    if get_card_value(card) == 6:
        return 7

    if get_card_value(card) == 7:
        return 7


card_labels = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

def swap_needed(card1, card2):
    if get_card_value_with_J(card1) > get_card_value_with_J(card2):
        return True
    elif get_card_value_with_J(card1) == get_card_value_with_J(card2): 
        for label in range(0,5):
            if card_labels.index(card1[label]) > card_labels.index(card2[label]):
                return True
            elif card_labels.index(card1[label]) < card_labels.index(card2[label]):
                return False
            else:
                continue
    else:
        return False


# sort cards
def bubbleSort(cards):
    n = len(cards)
    swapped = False

    for i in range(n-1):
        for j in range(0, n-i-1):
            if swap_needed(cards[j][0],cards[j+1][0]):
                swapped = True
                cards[j], cards[j+1] = cards[j+1], cards[j]
         
        if not swapped:
            return


bubbleSort(cards)
# print(cards)


for card_index, card in enumerate(cards):
    sum = sum + ((card_index + 1) * int(card[1]))

print("The sum is: ")
print(sum)
