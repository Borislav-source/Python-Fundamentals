txt = input()
result = []
instant_txt = []
number = []
for ch in range(len(txt)):
    if not txt[ch].isdigit():
        instant_txt.append(txt[ch].upper())
    else:
        number.append(txt[ch])
        if not ch + 1 == len(txt):
            if txt[ch + 1].isdigit():
                continue
        result.append(''.join(instant_txt) * int(''.join(number)))
        instant_txt.clear()
        number.clear()
print(f"Unique symbols used: {len(set(''.join(result)))}")
print(''.join(result))
