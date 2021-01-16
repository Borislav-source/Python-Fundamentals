my_dict = {}
data = input()
condition = False
while not data == 'Season end':
    if 'vs' in data:
        data = data.split(' vs ')
        player = data[0]
        player2 = data[1]
        if player in my_dict and player2 in my_dict:
            for posn in my_dict[player]:
                for posn2 in my_dict[player2]:
                    if posn == posn2:
                        if sum(my_dict[player].values()) > sum(my_dict[player2].values()):
                            del my_dict[player2]
                            condition = True
                        elif sum(my_dict[player].values()) < sum(my_dict[player2].values()):
                            del my_dict[player]
                            condition = True
                if condition:
                    break
    else:
        data = data.split(' -> ')
        player = data[0]
        position = data[1]
        skill = int(data[2])
        if player not in my_dict:
            my_dict[player] = {}
            my_dict[player][position] = skill
        else:
            if position not in my_dict[player]:
                my_dict[player][position] = skill
            elif my_dict[player][position] < skill:
                my_dict[player][position] = skill
    data = input()

for plr in dict(sorted(my_dict.items(), key= lambda x: (-sum(x[1].values()), x[0]))):
    print(f'{plr}: {sum(my_dict[plr].values())} skill')
    for pos in dict(sorted(my_dict[plr].items(), key= lambda x: (-x[1], x[0]))):
        print(f'- {pos} <::> {my_dict[plr][pos]}')