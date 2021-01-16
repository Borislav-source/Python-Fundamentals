num_of_lines = 3
game = []
vertical_list_1 = []
vertical_list_2 = []
vertical_list_3 = []
diagonal_list_1 = []
diagonal_list_2 = []
a = 2
condition = False
final_list = []
for n in range(num_of_lines):
    line = input().split()
    game.append(line)
    vertical_list_1.append(line[0])
    vertical_list_2.append(line[1])
    vertical_list_3.append(line[2])
    diagonal_list_1.append(line[n])
    diagonal_list_2.append(line[a])
    a -= 1
final_list += vertical_list_1, vertical_list_2, vertical_list_3, diagonal_list_1, diagonal_list_2
for elements in final_list:
    for i in range(len(elements)):
        if list(elements).count('1') == 3 or game[i].count('1') == 3:
            print('First player won')
            condition = True
            break
        elif list(elements).count('2') == 3 or game[i].count('2') == 3:
            print('Second player won')
            condition = True
            break
    if condition:
        break
if not condition:
    print('Draw!')





