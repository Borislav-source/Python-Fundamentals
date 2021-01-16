text = input()
my_dict = {}
for char in text:
    if not char == ' ':
        key = char
        value = text.count(char)
        my_dict[key] = value
for key, value in my_dict.items():
    print(f'{key} -> {value}')
