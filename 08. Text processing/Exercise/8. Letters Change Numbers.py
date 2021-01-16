NUM = 31


def positions(txt):
    for i in txt:
     return ord(i) & NUM


number = ''
first_letter = ''
last_letter = ''
txt = input().split()
for word in range(len(txt)):
    first_letter = txt[word][0]
    index_first = positions(first_letter)
    last_letter = txt[word][-1]
    index_last = positions(last_letter)
    for ch in txt[word]:
        if ch.isdigit():
            number += ch
    number = int(number)
    if first_letter.isupper():
        number /= index_first
    else:
        number *= index_first
    if last_letter.isupper():
        number -= index_last
    else:
        number += index_last
    txt[word] = str(number)
    number = ''
txt = [round(float(i), 3) for i in txt]
a = 5
print(f'{sum(txt):.2f}')


