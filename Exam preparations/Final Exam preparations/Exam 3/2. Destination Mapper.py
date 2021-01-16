import re
places = input()
pattern = r'(=|/)(?P<one>[A-Z][a-zA-Z]{2,})(\1)'
locations = re.finditer(pattern, places)
locs = [p.group('one') for p in locations]
points = [len(p) for p in locs]
print(f'''Destinations: {', '.join(locs)}
Travel Points: {sum(points)}''')
