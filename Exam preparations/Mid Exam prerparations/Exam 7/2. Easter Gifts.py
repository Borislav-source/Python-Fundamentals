gifts = input().split()
data = input()
while not data == 'No Money':
    command, gift, *index = data.split()
    if command == 'OutOfStock' and gift in gifts:
        gifts = [None if gifts[g] == gift else gifts[g] for g in range(len(gifts))]
    elif command == 'Required':
        index = int(''.join(index))
        if index in range(len(gifts)):
            gifts[index] = gift
    elif command == 'JustInCase':
        gifts.pop()
        gifts.append(gift)
    data = input()
[print(gif, end=' ') for gif in gifts if gif is not None]
