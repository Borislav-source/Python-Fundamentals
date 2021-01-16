input_txt = input()
old_ch = ''
result = ''
for ch in input_txt:
    if not ch == old_ch:
        result += ch
    old_ch = ch
print(result)
