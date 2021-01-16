import re
n = int(input())
count = 0
for _ in range(n):
    username = ''
    password = ''
    data = input()
    pattern = r"(U\$)(?P<username>[A-Z][a-z]{2,})(\1)(P\@\$)(?P<password>[a-zA-Z]{5,}\d+)(\4)"
    registration = re.finditer(pattern, data)
    for i in registration:
        username = i.group('username')
        password = i.group('password')
    if username:
        print('Registration was successful')
        print(f"Username: {username}, Password: {password}")
        count += 1
    else:
        print('Invalid username or password')
print(f'Successful registrations: {count}')