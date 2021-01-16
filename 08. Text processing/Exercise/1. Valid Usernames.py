users = input().split(', ')
for name in users:
    n = 0
    if 3 < len(name) < 16:
        for c in name:
            if c.isidentifier() or c.isdigit():
                n += 1
            elif c == '-':
                n += 1
            if len(name) == n:
                print(name)

