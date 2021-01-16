num = int(input())
condition = True
for i in range(2, num):
    if num % i == 0:
        condition = False
print(condition)
