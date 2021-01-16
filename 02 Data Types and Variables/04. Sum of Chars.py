count = int(input())
summ = 0
for i in range(0, count):
    char = input()
    summ += ord(char)
print(f'The sum equals: {summ}')