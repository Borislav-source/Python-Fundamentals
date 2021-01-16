year = int(input())
year += 1
year = str(year)
while len(set(year)) != len(year):
    year = int(year)
    year += 1
    year = str(year)
print(year)
