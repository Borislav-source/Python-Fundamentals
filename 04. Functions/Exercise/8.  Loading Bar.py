
def loading_bar(n):
    if n % 10 == 0:
        a = int(n / 10)
        my_list = []
        my_list.extend(['%' * int(a) + '.' * (10 - a)])
        return my_list[0]

n = int(input())
loading_bar(n)
if n == 100:
    print(f'''100% Complete!
[{loading_bar(n)}]''')
else:
    print(f'''{n}% [{loading_bar(n)}]
Still loading...''')