n = int(input())
heroes = {}
for _ in range(n):
    name, hp, mp = input().split()
    heroes[name] = [int(hp), int(mp)]
data = input()
while not data == 'End':
    data = data.split(" - ")
    action = data[0]
    hero_name = data[1]

    if action == 'CastSpell':
        mp_needed = int(data[2])
        spell_name = data[3]
        if heroes[hero_name][1] >= mp_needed:
            heroes[hero_name][1] -= mp_needed
            print(f'{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!')
        else:
            print(f'{hero_name} does not have enough MP to cast {spell_name}!')

    elif action == 'TakeDamage':
        damage = int(data[2])
        attacker = data[3]
        heroes[hero_name][0] -= damage
        if heroes[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]

    elif action == 'Recharge':
        amount = int(data[2])
        heroes[hero_name][1] += amount
        if heroes[hero_name][1] > 200:
            remaining = heroes[hero_name][1] - 200
            heroes[hero_name][1] = 200
            print(f"{hero_name} recharged for {amount - remaining} MP!")
        else:
            print(f"{hero_name} recharged for {amount} MP!")

    elif action == 'Heal':
        amount = int(data[2])
        heroes[hero_name][0] += amount
        if heroes[hero_name][0] > 100:
            remaining = heroes[hero_name][0] - 100
            heroes[hero_name][0] = 100
            print(f"{hero_name} healed for {amount - remaining} HP!")
        else:
            print(f"{hero_name} healed for {amount} HP!")
    data = input()
for key in dict(sorted(heroes.items(), key=lambda x: (-x[1][0], x[0]))):
    print(key)
    print(f"  HP: {heroes[key][0]}")
    print(f"  MP: {heroes[key][1]}")