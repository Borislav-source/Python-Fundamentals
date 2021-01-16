targets = list(map(int, input().split("|")))
data = input()
points = 0
while True:
    if data == "Game over":break
    command = data.split()
    type_command = command[0]
    if type_command == "Shoot":
        direction, a, b = command[1].split("@")
        start_index = int(a)
        length = int(b)
        if start_index in range(len(targets)):
            if direction == "Left": index = (start_index - length) % len(targets)
            else: index = (start_index + length) % len(targets)
            if targets[index] < 5:
                points += targets[index]
                targets[index] = 0
            else:
                targets[index] -= 5
                points += 5
    elif type_command == "Reverse":targets = list(map(str, reversed(targets)))
    data = input()
print(f"{' - '.join(targets)}\nIskren finished the archery tournament with {points} points!")
