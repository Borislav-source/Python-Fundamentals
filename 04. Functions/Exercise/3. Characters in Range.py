def ascii_alphabet(first_char, second_char):
    for characters in range(ord(first_char) + 1, ord(second_char)):
        print(chr(characters), end=" ")


first_char = input()
second_char = input()

ascii_alphabet(first_char, second_char)