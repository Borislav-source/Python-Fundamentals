def max_num(manipulation):
    for index in range(1, len(list_of_integers) + 1):
        if manipulation == 'even':
            if sorted(list_of_integers)[-index] % 2 == 0:
                biggest_even_num = sorted(list_of_integers)[-index]
                biggest_num = biggest_even_num
                return biggest_num
        else:
            if sorted(list_of_integers)[-index] % 2 != 0:
                biggest_odd_num = sorted(list_of_integers)[-index]
                biggest_num = biggest_odd_num
                return biggest_num


def min_num(manipulation):
    for index in range(len(list_of_integers)):
        if manipulation == 'even':
            if sorted(list_of_integers)[index] % 2 == 0:
                smallest_even_num = sorted(list_of_integers)[index]
                smallest_num = smallest_even_num
                return smallest_num
        else:
            if sorted(list_of_integers)[index] % 2 != 0:
                smallest_odd_num = sorted(list_of_integers)[index]
                smallest_num = smallest_odd_num
                return smallest_num


def count_of_first(manipulation, count):
    for index in range(len(list_of_integers)):
        if manipulation == 'even':
            if list_of_integers[index] % 2 == 0:
                list_of_first.extend([list_of_integers[index]])

        else:
            if list_of_integers[index] % 2 != 0:
                list_of_first.extend([list_of_integers[index]])
    return list_of_first[:count]


def count_of_last(manipulation, count):
    for index in range(1, len(list_of_integers) + 1):
        if manipulation == 'even':
            if list_of_integers[-index] % 2 == 0:
                list_of_last.extend([list_of_integers[-index]])

        else:
            if list_of_integers[-index] % 2 != 0:
                list_of_last.extend([list_of_integers[-index]])
    return list_of_last[:count]


line_of_integers = input().split()
list_of_integers = list(map(int, line_of_integers))
while True:
    manipulation = None
    variable = None
    command = input()
    if command == 'end':
        print(list_of_integers)
        break
    command_list = list(command.split())
    if command_list[0] == 'exchange':
        variable = int(command_list[1])
        if variable > 0:
            variable += 1
        if abs(variable) < len(list_of_integers):
            list1 = list_of_integers[:int(variable)]
            list2 = list_of_integers[int(variable):]
            list_of_integers = list2 + list1
        else:
            print('Invalid index')
    elif command_list[0] == 'max':
        manipulation = command_list[1]
        variable = max_num(manipulation)
        if variable is None:
            print('No matches')
        elif list_of_integers.count(variable) < 2:
            for index in range(len(list_of_integers)):
                if list_of_integers[index] == variable:
                    print(index)
                    break
        else:
            for index in range(len(list_of_integers)):
                if list_of_integers[-index] == variable:
                    print(-index)
                    break
    elif command_list[0] == 'min':
        manipulation = command_list[1]
        variable = min_num(manipulation)
        if variable is None:
            print('No matches')
        elif list_of_integers.count(variable) < 2:
            for index in range(len(list_of_integers)):
                if list_of_integers[index] == variable:
                    print(index)
                    break
        else:
            for index in range(len(list_of_integers)):
                if list_of_integers[-index] == variable:
                    print(-index)
                    break
    elif command_list[0] == 'first':
        manipulation = command_list[2]
        count = int(command_list[1])
        if abs(count) > len(list_of_integers):
            print('Invalid count')
            continue
        list_of_first = []
        variable = count_of_first(manipulation, count)
        print(variable)
    elif command_list[0] == 'last':
        manipulation = command_list[2]
        count = int(command_list[1])
        if abs(count) > len(list_of_integers):
            print('Invalid count')
            continue
        list_of_last = []
        variable = count_of_last(manipulation, count)
        print(variable)





