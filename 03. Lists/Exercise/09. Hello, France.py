items = input()
budget = float(input())
money = budget
profit = 0
list_of_items = items.split("|")
final_list = []
for i in range(len(list_of_items)):
    final_list.append(list_of_items[i].split("->"))
for j in range(len(final_list)):
    if final_list[j][0] == 'Clothes' and float(final_list[j][1]) <= 50:
        if budget >= float(final_list[j][1]):
            budget -= float(final_list[j][1])
            profit += float(final_list[j][1]) * 0.4
            print(f'{float(final_list[j][1]) * 0.4 + float(final_list[j][1]):.2f}', end=' ')
    elif final_list[j][0] == 'Shoes' and float(final_list[j][1]) <= 35:
        if budget >= float(final_list[j][1]):
            budget -= float(final_list[j][1])
            profit += float(final_list[j][1]) * 0.4
            print(f'{float(final_list[j][1]) * 0.4 + float(final_list[j][1]):.2f}', end=' ')
    elif final_list[j][0] == 'Accessories' and float(final_list[j][1]) <= 20.5:
        if budget >= float(final_list[j][1]):
            budget -= float(final_list[j][1])
            profit += float(final_list[j][1]) * 0.4
            print(f'{float(final_list[j][1])*0.4 + float(final_list[j][1]):.2f}', end=' ')
print(f'''
Profit: {profit:.2f}''')
a = money + profit
if a >= 150:
    print('Hello, France!')
else:
    print('Time to go.')
