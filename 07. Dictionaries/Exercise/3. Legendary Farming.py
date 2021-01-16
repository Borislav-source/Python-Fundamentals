my_dict = {}
legendaries = ['shards', 'fragments', 'motes']
condition = False
while True:
    items = input().split()
    for index in range(0, len(items), 2):
        key = items[index + 1].lower()
        value = int(items[index])
        if not key in my_dict:
            my_dict[key] = value
        else:
            my_dict[key] += value
        if key in legendaries and my_dict[key] >= 250:
            if my_dict[key] > 250:
                my_dict[key] -= 250
                if key == 'shards':
                    print('Shadowmourne obtained!')
                elif key == 'fragments':
                    print('Valanyr obtained!')
                else:
                    print('Dragonwrath obtained!')
            condition = True
            break
    if condition:
        break
junk = {ele: val for ele, val in my_dict.items() if ele not in legendaries}
second_dict = my_dict.copy()
for key in second_dict:
    if key in junk:
        my_dict.pop(key)
for key in legendaries:
    if key not in my_dict:
        my_dict[key] = 0
sorted_dict = dict(sorted(my_dict.items(), key= lambda x:(-x[1], x[0])))
a = {print(f'{ele}: {val}') for ele, val in sorted_dict.items() if ele in legendaries}
junk = dict(sorted(junk.items()))
b = {print(f'{key}: {val}') for key, val in junk.items()}
