text = input()
encrypted_version = ''
for ch in text:
    encrypted_version += chr(ord(ch) + 3)
print(encrypted_version)