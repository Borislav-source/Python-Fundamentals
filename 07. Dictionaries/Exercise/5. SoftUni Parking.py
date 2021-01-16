number_of_commands = int(input())
my_dict = {}
for number in range(number_of_commands):
    data = input().split()
    command = data[0]
    username = data[1]
    if command == 'register':
        licensePlate = data[2]
        if not username in my_dict:
            my_dict[username] = licensePlate
            print(f"{username} registered {licensePlate} successfully")
        else:
            print(f"ERROR: already registered with plate number {my_dict[username]}")
    elif command == 'unregister':
        if username in my_dict:
            print(f"{username} unregistered successfully")
            my_dict.pop(username)
        else:
            print(f"ERROR: user {username} not found")
for key in my_dict:
    print(f"{key} => {my_dict[key]}")