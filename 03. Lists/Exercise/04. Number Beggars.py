numbers = input()
beggars = int(input())
current_list = []
list_of_numbers = numbers.split(", ")
sum_list = []

for i in range(0, beggars):
    current_list.clear()
    for j in range(i, len(list_of_numbers), beggars):
        current_list.append(int(list_of_numbers[j]))
    a = sum(current_list)
    sum_list.append(a)
print(sum_list)

