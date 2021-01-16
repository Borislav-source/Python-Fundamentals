players_1 = []
players_2 = []
condition = False
for i in range(1, 12):
    players_1.append('A-' + str(i))
    players_2.append('B-' + str(i))
reserve = input()
new_list = reserve.split(" ")
for index in new_list:
    if index in players_1:
        players_1.remove(index)
    elif index in players_2:
        players_2.remove(index)
    if len(players_1) < 7:
        condition = True
        break
print(f'Team A - {len(players_1)}; Team B - {len(players_2)}')
if condition:
    print('Game was terminated')