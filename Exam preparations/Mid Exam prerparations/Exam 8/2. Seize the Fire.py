fire_cells = input()
amount_of_water = int(input())
list_1 = fire_cells.split("#")
final_list = []
list_of_variables = ['Effort =', 0, 'total_fire =', 0]
print('Cells:')
for i in range(len(list_1)):
    current_list = list(list_1[i].split(" = "))
    final_list.append(current_list)
for j in range(len(final_list)):
    if final_list[j][0] == 'High':
        if not 81 <= int(final_list[j][1]) <= 125:continue
    if final_list[j][0] == 'Medium':
        if not 51 <= int(final_list[j][1]) <= 80:continue
    if final_list[j][0] == 'Low':
        if not 1 <= int(final_list[j][1]) <= 50:continue
    if amount_of_water >= int(final_list[j][1]):
        amount_of_water -= int(final_list[j][1])
        list_of_variables[1] += int(final_list[j][1]) * 0.25
        list_of_variables[3] += int(final_list[j][1])
        print(f' - {int(final_list[j][1])}')
print(f'Effort: {(list_of_variables[1]):.2f}\nTotal Fire: {list_of_variables[3]}')
