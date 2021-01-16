import re

data = input()
word = input()

pattern = r"(?i)(\bword\b)"
pattern = pattern.replace('word', word)
matches = re.findall(pattern, data)

print(len(matches))