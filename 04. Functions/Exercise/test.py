# # def max_num(manipulation):
# #     for index in range(1, len(list_of_integers) + 1):
# #         if manipulation == 'even':
# #             if sorted(list_of_integers)[-index] % 2 == 0:
# #                 biggest_even_num = sorted(list_of_integers)[-index]
# #                 biggest_num = biggest_even_num
# #                 return biggest_num
# #
# #         else:
# #             if sorted(list_of_integers)[-index] % 2 != 0:
# #                 biggest_odd_num = sorted(list_of_integers)[-index]
# #                 biggest_num = biggest_odd_num
# #                 return biggest_num
# #
# #
# #
# # def min_num(manipulation):
# #     for index in range(1, len(list_of_integers) + 1):
# #         if manipulation == 'even':
# #             if sorted(list_of_integers)[index] % 2 == 0:
# #                 smallest_even_num = sorted(list_of_integers)[index]
# #                 smallest_num = smallest_even_num
# #                 return smallest_num
# #
# #         else:
# #             if sorted(list_of_integers)[index] % 2 != 0:
# #                 smallest_odd_num = sorted(list_of_integers)[index]
# #                 smallest_num = smallest_odd_num
# #                 return smallest_num
# #
# #
# # def count_of_first(manipulation, count):
# #     for index in range(len(list_of_integers)):
# #         if manipulation == 'even':
# #             if list_of_integers[index] % 2 == 0:
# #                 list_of_first.extend([list_of_integers[index]])
# #             return list_of_first[:count]
# #         else:
# #             if list_of_integers[index] % 2 != 0:
# #                 list_of_first.extend([list_of_integers[index]])
# #             return list_of_first[:count]
# #



# line_of_integers = input().split()
# list_of_integers = list(map(int, line_of_integers))
# # manipulation = input()
# # # print(max_num(manipulation))
# # list_of_first = []
# # print(count_of_first(manipulation, count))
# command_list1 = 1
# list1 = list_of_integers[:command_list1]
# list2 = list_of_integers[command_list1:]
# list_of_integers = list2 + list1
# print(list_of_integers)

list_a = [1, 2, 3, 4, 5, 6]
list1 = list_a[:0]
print(list1)