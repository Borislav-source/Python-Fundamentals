events_list = input().split("|")
energy = 100
coins = 100
condition = False

for event in events_list:
    command, value = event.split("-")
    value = int(value)
    if command == 'rest':
        if energy + value <= 100:
            energy += value
            print(f'You gained {value} energy.')
            print(f'Current energy: {energy}.')
        else:
            print(f'You gained {0} energy.')
            print(f'Current energy: {energy}.')
    elif command == 'order':
        if energy - 30 >= 0:
            coins += value
            energy -= 30
            print(f'You earned {value} coins.')
        else:
            energy += 50
            print('You had to rest!')
    elif 'order' != command != 'rest':
        coins -= value
        if coins >= 0:
            print(f'You bought {command}.')
        else:
            condition = True
            break
if condition:
    print(f'Closed! Cannot afford {command}.')
else:
    print(f'''Day completed!
Coins: {coins}
Energy: {energy}''')
