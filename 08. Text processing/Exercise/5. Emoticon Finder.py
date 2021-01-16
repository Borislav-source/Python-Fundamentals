text = input()
for ch in range(len(text)):
    if text[ch] == ':':
        print(text[ch] + text[ch+1])
