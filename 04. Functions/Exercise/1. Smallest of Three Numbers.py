import sys


def smallest_num():
    floor_number = sys.maxsize
    for number in range(3):
        num = int(input())
        if num < floor_number:
            floor_number = num
    return floor_number


print(smallest_num())
