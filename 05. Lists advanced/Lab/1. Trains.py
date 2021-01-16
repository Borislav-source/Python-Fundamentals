number_of_wagons = int(input())
train = [0 for _ in range(number_of_wagons)]
command = input()
while not command == 'End':
    command = command.split()
    if command[0] == 'add':
        train[-1] += int(command[1])
    elif command[0] == 'insert':
        index = int(command[1])
        value = int(command[2])
        train[index] += value
    elif command[0] == 'leave':
        index = int(command[1])
        value = int(command[2])
        train[index] -= value
    command = input()
print(train)

