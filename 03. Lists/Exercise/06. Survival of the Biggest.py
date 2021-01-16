numbers = input()
n = int(input())

list_of_numbers = numbers.split(" ")
list_of_numbers_map = map(int, list_of_numbers)
list_of_numbers= list(list_of_numbers_map)
list_of_numbers_2 = list_of_numbers.copy()
list_of_numbers_2.sort()

for i in range(n):
    list_of_numbers_2.pop(0)

for j in range(len(list_of_numbers)):
    if not list_of_numbers[j] in list_of_numbers_2:
        list_of_numbers[j] = None
    else:
        continue
final_list = list(dict.fromkeys(list_of_numbers))
final_list.remove(None)
print(final_list)
