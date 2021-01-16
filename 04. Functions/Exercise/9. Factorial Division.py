import math


def division(num1, num2):
    result = math.factorial(num1) / math.factorial(num2)
    return result


num1 = int(input())
num2 = int(input())
division(num1, num2)
print(f'{division(num1,num2): .2f}')