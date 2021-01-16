key = int(input())
n = int(input())
word = ''
for i in range(0, n):
    a = input()
    a = ord(a)
    a += key
    word += chr(a)
print(word)