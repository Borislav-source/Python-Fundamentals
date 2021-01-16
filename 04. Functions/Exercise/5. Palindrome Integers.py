def palindrome_search(list_of_nums):
    for element in list_of_nums:
        if element == element[:: -1]:
            print(True)
        else:
            print(False)


list_of_nums = input().split(", ")
palindrome_search(list_of_nums)