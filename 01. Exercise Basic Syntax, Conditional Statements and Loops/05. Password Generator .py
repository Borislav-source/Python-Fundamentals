n = int(input())
l = int(input())
first = ''
second = ''
txt = 'abcdefghijklmnopqrstuvwxyz'
for symbol1 in range(1, n):
    for symbol2 in range(1, n):
        for symbol3 in range(0, l):
            first = txt[symbol3]
            for symbol4 in range(0, l):
                second = txt[symbol4]
                for symbol5 in range(1, n + 1):
                    if symbol5 > symbol1 and symbol5 > symbol2:
                        print(f"{symbol1}{symbol2}{first}{second}{symbol5}", end = ' ' )
