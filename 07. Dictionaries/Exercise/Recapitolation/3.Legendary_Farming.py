resources = input().split()
junk_basket = {}
main_basket = {}
main_materials = ['shards', 'fragments', 'motes']


def recalculation(material):
    if material == 'shards':
        obtained_material = 'Shadowmourne'
    elif material == 'fragments':
        obtained_material = 'Valanyr'
    else:
        obtained_material = 'Dragonwrath'

    return obtained_material


while resources:
    for index in range(1, len(resources), 2):
        material = resources[index].lower()
        value = int(resources[index - 1])
        if material in main_materials:
            if material not in main_basket:
                main_basket[material] = value
            else:
                main_basket[material] += value
            if value >= 250:
                main_basket[material] -= 250
                obtained_material = recalculation(material)
                break
        elif material not in junk_basket:
            junk_basket[material] = value
    resources = input().split()

print(f'{obtained_material} is obtained!')
sorted_basket = dict(sorted(main_basket.items(), key= lambda x: (x[1], x[0]), reverse=True))
print(sorted_basket)
