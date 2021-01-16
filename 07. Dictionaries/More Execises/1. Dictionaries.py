line = input()
contest_dict = {}
users_contest = {}
while not line == 'end of contests':
    contest, password = line.split(':')
    contest_dict[contest] = password
    line = input()
data = input()
while not data == 'end of submissions':
    contest, password, username, points = data.split('=>')
    points = int(points)
    if contest in contest_dict:
        if contest_dict[contest] == password:
            if username not in users_contest:
                users_contest[username] = {}
                users_contest[username][contest] = points
            elif contest in users_contest[username]:
                for con in users_contest[username]:
                    if contest == con:
                        if points > users_contest[username][con]:
                            users_contest[username][con] = points
            else:
                users_contest[username][contest] = points
    data = input()
best = 0
for user in users_contest:
    total = 0
    for contest in users_contest[user]:
        total += users_contest[user][contest]
    if total > best:
        best = total
        the_user = user
print(f'Best candidate is {the_user} with total {best} points.')
print('Ranking:')
for student in dict(sorted(users_contest.items(), key=lambda x: x[0])):
    print(student)
    for con in dict(sorted(users_contest[student].items(), key=lambda x: x[1], reverse=True)):
        print(f'#  {con} -> {users_contest[student][con]}')
