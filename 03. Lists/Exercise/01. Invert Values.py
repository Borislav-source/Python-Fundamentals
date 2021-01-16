numbers = input()
my_list = numbers.split(' ')
new_list = []
for number in my_list:
    new_list.append(int(number) * -1)
print(new_list)