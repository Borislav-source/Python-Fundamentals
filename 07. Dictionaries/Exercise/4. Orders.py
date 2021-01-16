data = input()
my_dict = {}
while not data == 'buy':
    product, price, quantity = data.split()
    key = product
    if key in my_dict:
        my_dict[key][1] += int(quantity)
        my_dict[key][0] = float(price)
    else:
        value = [float(price), int(quantity)]
        my_dict[key] = value
    data = input()
for key in my_dict:
    my_dict[key] = my_dict[key][0] * my_dict[key][1]
    print(f'{key} -> {my_dict[key]:.2f}')