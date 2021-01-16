targets = list(map(int, input().split()))
while True:
    data = input()
    if data == 'End':
        break
    command, index, value = data.split()
    index = int(index)
    value = int(value)
    if command == 'Shoot':
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.remove(targets[index])
    elif command == 'Add':
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else: print('Invalid placement!')
    elif command == 'Strike':
        if index - value >= 0 and index + value < len(targets):
            targets = targets[:index - value] + targets[index + value + 1:]
        else: print('Strike missed!')
print("|".join(list(map(str, targets))))
