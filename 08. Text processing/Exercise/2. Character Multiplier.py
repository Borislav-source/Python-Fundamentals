words = input().split()
the_sum = 0
condition = False
test = words[0]
if len(words[1]) < len(words[0]):
    test = words[1]
    condition = True
for index in range(len(test)):
    the_sum += ord(words[0][index]) * ord(words[1][index])
if condition:
    for ch in words[0][len(test):]:
        the_sum += ord(ch)
else:
    for ch in words[1][len(test):]:
        the_sum += ord(ch)
print(the_sum)