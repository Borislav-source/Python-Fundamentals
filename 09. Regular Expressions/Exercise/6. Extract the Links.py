import re
links_list = []
data = input()
while data:
    pattern = r"www\.[a-zA-Z0-9-][a-zA-Z0-9.-]+\.[a-z]+"
    links = re.findall(pattern, data)
    if any(links):
        links_list.append(links)
    data = input()

for l in links_list:
    print(*l)