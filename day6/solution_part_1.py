sum = 1

def get_times():
    pass

def get_distances():
    pass

# times = [7, 15, 30]
# distances = [9, 40, 200]

times = [55, 99, 97, 93]
distances = [401, 1485, 2274, 1405]

for time_index, time in enumerate(times):

    print(time)

    potantial_wins = 0
    for x in range(1, time):
        if x * (time - x) > distances[time_index]:
            potantial_wins = potantial_wins + 1
    
    print(potantial_wins)
    sum = sum * potantial_wins
            
    
print("The answer is: ")
print(sum)