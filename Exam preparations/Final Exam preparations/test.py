# a = 'longlongTESTstringTEST'
# a = a.replace('TEST', '?')
# print(a)
# import re
# text = input()
# mirrors = []
# patten = r"(@|#)(?P<one>[a-zA-Z]{3,})(\1)(\1)(?P<two>[a-zA-Z]{3,})(\1)"
# words = re.finditer(patten, text)
# for word in words:
#     if word.group('one') == word.group('two')[::-1]:
#         sequence = word.group('one') + " <=> " + word.group('two')
#         mirrors.append(sequence)
# print(mirrors)

# data = input()
#
# while not data == 'Stop':
#     data = data.split(' : ')
#     command, car = data[:2]
#     if command == 'drive':
#        distance, fuel = [int(i) for i in data[2:]]
#     data = input()
# a = [1, 23, 24]
# b, c = a[1:]
# print(b, c)
message = 'asdfa'
data = input()
num_of_letters = int(data)
sub = message[:num_of_letters]
message = message[num_of_letters:]
message += sub
print(message)