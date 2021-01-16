software = list(map(int, input().split('.')))

for i in range(1, len(software) + 1):
    if software[-i] == 9:
        software[-i] = software[i] * 0
    else:
        software[-i] += 1
        break
[print(software[num]) if num == (len(software) -1) else print(software[num], end='.') for num in range(len(software))]
