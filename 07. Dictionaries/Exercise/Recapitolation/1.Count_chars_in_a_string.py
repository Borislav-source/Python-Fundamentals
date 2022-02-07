text = list(input())
my_dict = {}

for character in text:
    if character not in my_dict:
        my_dict[character] = 1
    else:
        my_dict[character] += 1

for a, b in my_dict.items():
    print(f'{a} -> {b}')
