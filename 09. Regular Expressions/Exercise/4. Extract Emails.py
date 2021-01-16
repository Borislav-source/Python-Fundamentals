import re
emails = input()

pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[-_\.a-zA-Z]+[a-zA-Z0-9]+@[a-z]+[\.-]?[\.a-z-]+[a-z]+\.[a-z]+"
matches = re.finditer(pattern, emails)
for match in matches:
    print(match.group())