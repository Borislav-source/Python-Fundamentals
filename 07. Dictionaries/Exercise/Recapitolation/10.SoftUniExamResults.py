text_input = input()
contestants_dict = {}
contest_dict = {}

while not text_input == 'exam finished':
    text_input = text_input.split("-")
    user, course, *result = text_input

    if result:
        result = int(result[0])
        if user not in contestants_dict:
            contestants_dict[user] = result
        else:
            if contestants_dict[user] < result:
                contestants_dict[user] = result

        if course not in contest_dict:
            contest_dict[course] = 1
        else:
            contest_dict[course] += 1
    else:
        contestants_dict.pop(user)
    text_input = input()

contestants_dict = dict(sorted(contestants_dict.items(), key=lambda x: (-x[1], x[0])))

print('Results:')

for key, value in contestants_dict.items():
    print(f'{key} | {value}')

for key, value in sorted(contest_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f'{key} - {value}')

