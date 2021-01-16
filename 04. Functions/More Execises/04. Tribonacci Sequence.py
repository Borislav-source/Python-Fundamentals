def tribonaci_sequence(num):
    list_of_numbers = [1, 1, 2]
    if num == 1:
        print(1)
        return
    elif num == 2:
        print(f'{1} {1}')
        return
    elif num == 3:
        print(list_of_numbers)
        return
    for number in range(num - 3):
        new_num = list_of_numbers[number] + list_of_numbers[number + 1] + list_of_numbers[number + 2]
        list_of_numbers.append(new_num)
    for element in range(len(list_of_numbers)):
        print(list_of_numbers[element], end=' ')


num = int(input())
tribonaci_sequence(num)