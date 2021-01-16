a = int(input())
b = int(input())

for i in range(b, 0, -1):
    total = i / a
    if total % 1 == 0:
        break
print(i)

