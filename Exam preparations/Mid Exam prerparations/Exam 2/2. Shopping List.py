groceries = input().split("!")

data = input()

while True:
    if data == "Go Shopping!":
        break
    command = data.split()[0]
    item = data.split()[1]
    if command == 'Urgent':
        if item not in groceries:
            groceries.insert(0, item)
    elif command == 'Unnecessary':
        if item in groceries:
            groceries.remove(item)
    elif command == 'Correct':
        old_item = item
        new_item = data.split()[2]
        if old_item in groceries:
            for i in range(len(groceries)):
                if groceries[i] == old_item:
                    groceries[i] = new_item
                    break
    elif command == 'Rearrange':
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)
    data = input()
print(', '.join(groceries))
