shops = input().split()
for commands in range(int(input())):
    command = input().split()
    typeof_command = command[0]
    if typeof_command == 'Include':
        shops.append(command[1])
    elif typeof_command == 'Visit' and len(shops) >= int(command[2]):
        for i in range(1, int(command[2]) + 1):
            if command[1] == 'first':
                shops.remove(shops[0])
            else:
                shops.remove(shops[-1])
    elif typeof_command == 'Prefer' and int(command[1]) in range(len(shops)) and int(command[2]) in range(len(shops)):
        shops[int(command[1])], shops[int(command[2])] = shops[int(command[2])], shops[int(command[1])]
    elif typeof_command == 'Place':
        index = int(command[2]) + 1
        if index in range(len(shops)):
            shops.insert(index, command[1])
print(f"Shops left:\n{' '.join(shops)}")
