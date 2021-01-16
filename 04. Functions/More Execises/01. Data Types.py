def type_of_integer(num):
    result = int(num) * 2
    print(result)


def type_of_real(num):
    result = float(num) * 1.5
    print(f'{result:.2f}')


def type_of_sting(num):
    print(f'${num}$')


command = input()
num = input()
if command == 'int':
    type_of_integer(num)
elif command == 'real':
    type_of_real(num)
else:
    type_of_sting(num)
