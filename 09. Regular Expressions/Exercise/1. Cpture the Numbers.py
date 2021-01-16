import re
data = input()
numbers = []
while data:
    regex = r"\d+"
    matches = re.findall(regex, data)
    numbers.extend(matches)
    data = input()
print(*numbers, end=' ')
