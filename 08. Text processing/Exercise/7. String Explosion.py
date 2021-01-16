text = input()
text = [i for i in text]
for ch in range(len(text)):
    if text[ch] is '>':
        position = ch
        if ch + 1 < len(text):
            if text[ch + 1].isdigit():
                number = int(text[ch + 1])
            else:
                continue
        else:
            continue
        n = 0
        for index in range(1, number + 1):
            if index + position in range(len(text)):
                if not text[index + position] == '>':
                    text[index + ch] = 'None'
                    n += 1
                elif text[index + position] == '>':
                    if n < number:
                        text[index + position + 1] = str(int(text[index + position + 1]) + (number - n))
                        break
text = [i for i in text if not i == 'None']
print(''.join(text))
