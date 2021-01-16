paintings = input().split()
data = input()

while not data == "END":
    data = data.split()
    command = data[0]
    if command == "Change":
        painting_number = data[1]
        changed_number = data[2]
        if painting_number in paintings:
            for index in range(len(paintings)):
                if paintings[index] == painting_number:
                    paintings[index] = changed_number
                    break
    elif command == 'Hide':
        painting_number = data[1]
        if painting_number in paintings:
            paintings.remove(painting_number)
    elif command == 'Switch':
        painting_number = data[1]
        painting_number2 = data[2]
        if painting_number in paintings and painting_number2 in paintings:
            for index in range(len(paintings)):
                if paintings[index] == painting_number:
                    paintings[index] = painting_number2
                elif paintings[index] == painting_number2:
                    paintings[index] = painting_number
    elif command == 'Insert':
        place = int(data[1]) + 1
        painting_number = data[2]
        if place in range(len(paintings)):
            paintings.insert(place, painting_number)
    elif command == 'Reverse':
        paintings = paintings[::-1]
    data = input()
print(' '.join(paintings))
