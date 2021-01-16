key = input()
my_dict = {}
while not key == 'stop':
    if not key in my_dict:
        value = int(input())
        my_dict[key] = value
    else:my_dict[key] += int(input())
    key = input()
for key, value in my_dict.items():print(f'{key} -> {value}')
