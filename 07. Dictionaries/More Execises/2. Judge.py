data = input()
contest_list = {}
users_list = {}
while not data == 'no more time':
    username, contest, points = data.split(' -> ')
    points = int(points)
    users_list[username] = 0
    if contest not in contest_list:
        contest_list[contest] = {}
        contest_list[contest][username] = points
    else:
        if username in contest_list[contest]:
            if contest_list[contest][username] < points:
                contest_list[contest][username] = points
        else:
            contest_list[contest][username] = points

    data = input()

for con in contest_list:
    print(f'{con}: {len(contest_list[con])} participants')
    n = 0
    for name in dict(sorted(contest_list[con].items(), key=lambda x: (-x[1], x[0]))):
        n += 1
        print(f'{n}. {name} <::> {contest_list[con][name]}')
        users_list[name] += contest_list[con][name]
print('Individual standings:')
n = 0
for name in dict(sorted(users_list.items(), key=lambda x: (-x[1], x[0]))):
    n += 1
    print(f'{n}. {name} -> {users_list[name]}')
