num_of_fills = int(input())
capacity = 255

for i in range(0, num_of_fills):
    liters = int(input())
    if capacity < liters:
        print('Insufficient capacity!')
    else:
        capacity -= liters
print(255 - capacity)