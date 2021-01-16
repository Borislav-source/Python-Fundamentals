def sign_of_num(list_of_nums):
    result = ''
    count_of_negative = 0

    for element in range(len(list_of_nums)):
        if list_of_nums[element] < 0:
            result = 'negative'
            count_of_negative += 1
        if list_of_nums[element] == 0:
            result = 'zero'
            break

        if count_of_negative < 1:
             result = 'positive'
        elif count_of_negative % 2 == 0:
            result = 'positive'
        else:
            result = 'negative'
    return result


num1 = float(input())
num2 = float(input())
num3 = float(input())
list_of_nums = [num1, num2, num3]

print(sign_of_num(list_of_nums))
