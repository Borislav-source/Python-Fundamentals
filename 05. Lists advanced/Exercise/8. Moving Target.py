targets = list(map(int, input().split()))
data = input()
while not data == 'End':
    data = data.split()
    command = data[0]
    index = int(data[1])
    value = int(data[2])
    if command == 'Shoot':
        if len(targets) > index >= 0:
            targets[index] -= value
            if targets[index] <= 0:
                targets.remove(targets[index])
    elif command == 'Add':
        if len(targets) > index >= 0:
            targets.insert(index, value)
        else: print('Invalid placement!')
    elif command == 'Strike':
        if index + value < len(targets) and index - value >= 0:
            targets = targets[:index - value] + targets[index + value + 1:]
        else: print('Strike missed!')
    data = input()
print("|".join(map(str, targets)))
