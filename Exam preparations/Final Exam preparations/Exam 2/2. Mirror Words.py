import re
text = input()
mirrors = []
patten = r"(@|#)(?P<one>[a-zA-Z]{3,})(\1)(\1)(?P<two>[a-zA-Z]{3,})(\1)"
words = re.finditer(patten, text)

if any(re.findall(patten, text)):
    print(f'{len(re.findall(patten, text))} word pairs found!')
    for word in words:
        if word.group('one') == word.group('two')[::-1]:
            sequence = word.group('one') + " <=> " + word.group('two')
            mirrors.append(sequence)
else:
    print('No word pairs found!')

if any(mirrors):
    print(f"The mirror words are:\n{', '.join(mirrors)}")
else:
    print('No mirror words!')