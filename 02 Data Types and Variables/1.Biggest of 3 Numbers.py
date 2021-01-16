b = 0
k = 0
while not k == 3:
    num = int(input())
    if num > b or num < 0 and b == 0:
        b = num
    k += 1
print(b)
