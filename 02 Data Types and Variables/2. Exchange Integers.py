a = int(input())
b = int(input())
c = None
d = None
c = a
d = b
a = d
b = c
print(f'''Before:
a = {b}
b = {a}
After:
a = {a}
b = {b}''')