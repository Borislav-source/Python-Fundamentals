email_dict = {}
data = input()
while not data == 'Statistics':
    data = data.split('->')
    command, username = data[:2]
    if command == 'Add':
        if not username in email_dict:
            email_dict[username] = []
        else:
            print(f"{username} is already registered")
    elif command == 'Send':
        email = data[2]
        email_dict[username].append(email)
    elif command == 'Delete':
        if username in email_dict:
            del email_dict[username]
        else:
            print(f'{username} not found!')
    data = input()
print(f'Users count: {len(email_dict)}')

for usr in dict(sorted(email_dict.items(), key=lambda x: (-len(x[1]), x[0]))):
    print(usr)
    for em in email_dict[usr]:
        print(f' - {em}')
