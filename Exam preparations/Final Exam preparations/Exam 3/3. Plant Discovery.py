n = int(input())
plant_dict = {}
for _ in range(n):
    plant, rarity = input().split('<->')
    plant_dict[plant] = [int(rarity), []]
data = input()
while not data == 'Exhibition':
    data = data.split(': ')
    command = data[0]
    if command == 'Rate':
        current_plant, rating = data[1].split(' - ')
        if current_plant in plant_dict:
            plant_dict[current_plant][1].append(int(rating))
        else:
            print('error')
    elif command == 'Update':
        current_plant, newrarity = data[1].split(' - ')
        if current_plant in plant_dict:
            plant_dict[current_plant][0] = int(newrarity)
        else:
            print('error')
    elif command == 'Reset':
        current_plant = data[1]
        if current_plant in plant_dict:
            plant_dict[current_plant][1] = [0]
        else:
            print('error')
    data = input()
for plant in plant_dict:
    if not sum(plant_dict[plant][1]) <= 0:
        plant_dict[plant][1] = sum(plant_dict[plant][1]) / len(plant_dict[plant][1])
    else:
        plant_dict[plant][1] = 0
print('Plants for the exhibition:')
for p in dict(sorted(plant_dict.items(), key=lambda x: (-x[1][0], -x[1][1]))):
    print(f'- {p}; Rarity: {plant_dict[p][0]}; Rating: {plant_dict[p][1]:.2f}')
