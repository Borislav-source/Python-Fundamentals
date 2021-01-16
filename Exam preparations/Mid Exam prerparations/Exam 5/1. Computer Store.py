total = 0
no_tax = 0
while True:
    order = input()
    if 'special' == order or order == 'regular':
        break
    order = float(order)
    if order < 0:
        print("Invalid price!")
        continue
    no_tax += order
    total += (order * 1.2)
tax = total - no_tax
if order == 'special':
    total *= 0.9
if total > 0:
    print(f'''Congratulations you've just bought a new computer! 
Price without taxes: {no_tax:.2f}$ 
Taxes: {tax:.2f}$ 
----------- 
Total price: {total:.2f}$
''')
else:
    print("Invalid order!")
