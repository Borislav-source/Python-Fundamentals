# # a = list(map(int, input().split()))
# # print(max(a))
# # print(min(a))
# # print(list(enumerate(a)))
# # a = [10, 10, 10, 10, 10]
# # c = 12
# # n = 0
# # si = 0
# # c += si + 1
# # while n != c:
# #     for i in range(len(a)):
# #         n += 1
# #         if n == c:
# #             a[-i] -= 5
# #             break
# # print(a)
#
# targets = list(map(int, input().split("|")))
# data = input()
# points = 0
# while data != "Game over":
#     n = 0
#     command = data.split("@")[0]
#     if command == "Shoot Right":
#         a = data.split("@")[1]
#         start_index = int(a)
#         b = data.split("@")[2]
#         length = int(b)
#         length += start_index + 1
#         if start_index in range(len(targets)):
#             while n != length:
#                 for i in range(len(targets)):
#                     n += 1
#                     if n == length:
#                         targets[i] -= 5
#                         points += 5
#                         break
#     elif command == "Shoot Left":
#         a = data.split("@")[1]
#         start_index = int(a)
#         b = data.split("@")[2]
#         length = int(b)
#         length += start_index + 1
#         if start_index in range(len(targets)):
#             while n != length:
#                 for i in range(len(targets)):
#                     n += 1
#                     if n == length:
#                         if targets[-i] < 5:
#                             points += targets[-i]
#                             targets[-i] = 0
#                         else:
#                             targets[-i] -= 5
#                             points += 5
#                         break
#     elif command == "Reverse":
#         targets = list(map(str, reversed(targets)))
#     data = input()
# print(f"{' - '.join(targets)}\nIskren finished the archery tournament with {points} points!")
# i1 = 'a'
# i2 = 'c'
# a = ['a', 'b', 'c', 'd']
# if i1 in a and i2 in a:
#     for i in range(len(a)):
#         if a[i] == i1:
#             a[i] = i2
#         elif a[i] == i2:
#             a[i] = i1
# print(a)

a = ['a', 'bcd', 'ab', 'abcd', 'b']
a.sort(reverse=True)
print(a)