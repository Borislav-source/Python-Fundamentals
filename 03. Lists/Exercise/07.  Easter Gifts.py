gifts = input()
list_of_gifts = gifts.split()
command = input()
while not command == 'No Money':
    command_list = command.split()
    if 'OutOfStock' in command_list:
         if command_list[1] in list_of_gifts:
            for i in range(len(list_of_gifts)):
                if list_of_gifts[i] == command_list[1]:
                    list_of_gifts[i] = None
    elif 'Required' in command_list:
        a = command_list[2]
        if int(a) <= len(list_of_gifts) - 1 and int(a) > 0:
            list_of_gifts[int(a)] = command_list[1]
    elif 'JustInCase' in command_list:
        list_of_gifts.pop()
        list_of_gifts.append(command_list[1])
    command = input()
for i in range(len(list_of_gifts)):
    if not list_of_gifts[i] == None:
        print(list_of_gifts[i], end=' ')
