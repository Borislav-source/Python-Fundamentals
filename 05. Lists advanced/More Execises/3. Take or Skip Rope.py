def find_digits(data):
    result = []

    for dig in range(len(data)):
        if data[dig].isdigit():
            result.append(int(data[dig]))
            data[dig] = None
    return result


data = list(input())
digits_list = find_digits(data)
data = [i for i in data if not i == None]
result = []
for ele in range(len(digits_list)):
    value = digits_list[ele]
    if value > len(data):
        value = len(data)
    if ele % 2 == 0:
        for k in range(value):
            result.append(data[k])
            data[k] = None
    else:
        for i in range(value):
            data[i] = None
    data = [data[j] for j in range(len(data)) if not data[j] == None]

[print(l, end='') for l in result if not l == '']
