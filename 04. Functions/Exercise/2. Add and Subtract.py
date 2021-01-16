def sum_numbers(num1, num2):
    result = num1 + num2
    return result


def subtract(result, num3):
    result -= num3
    return result


num1 = int(input())
num2 = int(input())
num3 = int(input())

result = sum_numbers(num1, num2)
print(subtract(result, num3))