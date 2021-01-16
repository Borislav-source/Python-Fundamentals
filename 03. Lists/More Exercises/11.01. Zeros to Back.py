list_of_integer = input().split(", ")
for element in list_of_integer:
    if element == '0':
        list_of_integer.remove(element)
        list_of_integer.append(element)
list_of_integer_map = list(map(int, list_of_integer))
print(list_of_integer_map)