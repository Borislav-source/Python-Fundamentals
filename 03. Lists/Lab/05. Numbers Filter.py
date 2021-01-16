num = int(input())
k = 0
list_of_number = list()
final_list_of_number = list()
current_number = input()
while k < num:
    current_number = int(current_number)
    list_of_number.append(current_number)
    k += 1
    current_number = input()

if current_number == 'even':
    for number in list_of_number:
        if number % 2 == 0:
            final_list_of_number.append(number)
elif current_number == 'odd':
    for number in list_of_number:
        if not number % 2 == 0:
            final_list_of_number.append(number)
elif current_number == 'positive':
    for number in list_of_number:
        if number >= 0:
            final_list_of_number.append(number)
elif current_number == 'negative':
    for number in list_of_number:
        if not number >= 0:
            final_list_of_number.append(number)
print(final_list_of_number)