data = input()
my_dict = {}
while not data == 'Lumpawaroo':
    if ' -> ' in data:
        user, side = data.split(" -> ")
        if [True for key in my_dict if user in my_dict[key]]:
            for key in my_dict:
                if user in my_dict[key]:
                    my_dict[key].remove(user)
        my_dict[side].append(user)
        print(f"{user} joins the {side} side!")
    elif ' | ' in data:
        side, user = data.split(' | ')
        if user not in my_dict:
            my_dict[side] = [user]
    data = input()
for key in my_dict:
    my_dict[key].sort()
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0])))
for key in sorted_dict:
    if len(sorted_dict[key]) > 0:
        print(f'Side: {key}, Members: {len(sorted_dict[key])}')
        for index in range(len(sorted_dict[key])):
            print(f'! {sorted_dict[key][index]}')

