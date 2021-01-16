initial_loot = input().split('|')
data = input()
stolen = []
items_len = 0
while not data == 'Yohoho!':
    data = data.split()
    command = data[0]
    if command == 'Loot':
        for el in range(1, len(data)):
            if not data[el] in initial_loot:
                initial_loot.insert(0, data[el])
    elif command == 'Drop':
        index = int(data[1])
        if index >= 0:
            if index in range(len(initial_loot)):
                item = initial_loot[index]
                initial_loot.remove(item)
                initial_loot.append(item)
        elif index < 0:
            if abs(index) in range(len(initial_loot) + 1):
                item = initial_loot[index]
                initial_loot.remove(item)
                initial_loot.append(item)
    elif command == 'Steal':
        count = int(data[1])
        if not count >= len(initial_loot):
            for ele in range(1, count + 1):
                stolen.append(initial_loot[-1])
                initial_loot.remove(initial_loot[-1])
            print(', '.join(stolen[::-1]))
        else:
            stolen = initial_loot
            print(', '.join(stolen))
            initial_loot.clear()
        stolen.clear()
    data = input()
if not len(initial_loot) == 0:
    for element in initial_loot:
        items_len += len(element)
    average = items_len / len(initial_loot)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
else:
    print('Failed treasure hunt.')


