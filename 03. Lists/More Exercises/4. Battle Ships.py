list_of_ships = []
number_of_rows = int(input())
number_of_fallen_ships = 0
for row in range(number_of_rows):
    ships_on_row = input().split()
    ships_on_row = map(int, ships_on_row)
    ships_on_row = list(map(int, ships_on_row))
    list_of_ships.extend([ships_on_row])

list_of_attack = []
attack = input().split()
new_attack_list = []
for ele in range(len(attack)):
    result = attack[ele].split("-")
    result = list(map(int, result))
    new_attack_list.append(result)

for element in range(len(new_attack_list)):
    if abs(new_attack_list[element][0]) == 0:
        coordinate = abs(new_attack_list[element][1])
        if list_of_ships[0][coordinate] > 0:
            list_of_ships[0][coordinate] -= 1
            if list_of_ships[0][coordinate] == 0:
                number_of_fallen_ships += 1

    elif abs(new_attack_list[element][0]) == 1:
        coordinate = abs(new_attack_list[element][1])
        if list_of_ships[1][coordinate] > 0:
            list_of_ships[1][coordinate] -= 1
            if list_of_ships[1][coordinate] == 0:
                number_of_fallen_ships += 1

    elif abs(new_attack_list[element][0]) == 2:
        coordinate = abs(new_attack_list[element][1])
        if list_of_ships[2][coordinate] > 0:
            list_of_ships[2][coordinate] -= 1
            if list_of_ships[2][coordinate] == 0:
                number_of_fallen_ships += 1
print(number_of_fallen_ships)