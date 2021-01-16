rooms_count = int(input())
condition = False
res = 0
for room in range(1, rooms_count + 1):
    chairs = input().split()
    occupied_chairs = int(chairs[1])
    number_of_chairs = len(chairs[0])
    if number_of_chairs == occupied_chairs:
        continue
    elif number_of_chairs > occupied_chairs:
        res += number_of_chairs - occupied_chairs
    else:
        condition = True
        needed = occupied_chairs - number_of_chairs
        print(f'{needed} more chairs needed in room {room}')
if not condition:
    print(f'Game On, {res} free chairs left')