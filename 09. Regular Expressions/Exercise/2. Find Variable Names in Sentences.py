import re
data = input()
regex = r"\b_([a-zA-Z0-9]+\b)"
matches = re.findall(regex, data)
print(','.join(matches))
