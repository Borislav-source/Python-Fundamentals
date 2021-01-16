electrons_input = int(input())
result_list = []

for index in range(1, electrons_input):
    res = lambda x: 2 * index ** 2
    if electrons_input - res(index) >= 0:
        result_list.append(res(index))
        electrons_input -= res(index)
        if electrons_input == 0:
            break
    else:
        remaining = res(index) - electrons_input
        result_list.append(res(index) - remaining)
        break
print(result_list)
