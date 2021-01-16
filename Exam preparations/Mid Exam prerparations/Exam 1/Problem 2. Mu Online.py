dungeons = input().split("|")
initial_health = 100
initial_coins = 0
condition = True

for room in range(len(dungeons)):
    command, number = dungeons[room].split()
    power = int(number)

    if command == "potion":
        initial_health += power
        if initial_health > 100:
            power -= initial_health - 100
            initial_health = 100
        print(f"You healed for {power} hp.\nCurrent health: {initial_health} hp.")
    elif command == "chest":
        initial_coins += power
        print(f'You found {power} bitcoins.')
    else:
        initial_health -= power
        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f'You died! Killed by {command}.\nBest room: {room + 1}')
            condition = False
            break

if condition:
    print(f"You've made it!\nBitcoins: {initial_coins}\nHealth: {initial_health}")

