list_of_numbers = list(map(int, input().split(', ')))
n = 0
while len(list_of_numbers) > 0:
    n += 10
    current_list = []
    for index in range(len(list_of_numbers)):
        number = list_of_numbers[index]
        if number <= n:
            current_list.append(number)
            list_of_numbers[index] = None
    list_of_numbers = [ele for ele in list_of_numbers if not ele == None]
    print(f"Group of {n}'s: {current_list}")
