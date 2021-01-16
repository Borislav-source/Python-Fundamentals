# a = '123ab12_-c1'
# for i in a:
#     if i.isidentifier():
#         print(i)
# print(a.isdigit())

# print(ord('a') * ord('a') + 3 * ord('a'))
# a = ['aaaa', 'bbb']
# for i in a:
#     print(a.count('a'))
#     print(a.count('b'))
# # print(round(a, 1))
NUM = 31
def positions(txt):
    for i in txt:
        print(ord(i) & NUM)
txt = 'abv'
positions(txt)
