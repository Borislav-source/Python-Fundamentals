numbers = input().split()
# numbers = list(map(int, numbers))
k = int(input())
final_list = []
new_list = numbers * (k + 1)
row = 0
f = -1
a = ''

for element in new_list:
    for i in new_list:
        if i == 'a':
            new_list.remove(i)
    row += 1
    if row % k == 0:
        final_list.append(element)
        row -= 2
        a = element

print(final_list)
