# from _collections import OrderedDict
# first_list = input().split(", ")
# second_list = input().split(", ")
# new_list = []
# for el in first_list:
#     for el2 in second_list:
#         if el in el2:
#             new_list.append(el)
# print(list(OrderedDict.fromkeys(new_list)))

first_list = input().split(", ")
second_list = input().split(", ")
new_list = []
for el in first_list:
    for el2 in second_list:
        if el in el2:
            new_list.append(el)
[new_list.remove(n) for n in new_list if new_list.count(n) > 1]
print(new_list)
