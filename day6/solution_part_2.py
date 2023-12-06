time = 55999793
distance = 401148522741405

print(time)

potantial_wins = 0
for x in range(1, time):
    if x * (time - x) > distance:
        potantial_wins = potantial_wins + 1

print(potantial_wins)