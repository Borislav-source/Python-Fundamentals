string1 = input()
string2 = input()
index_string_2 = ''
index_string = ''
old_str = ''
new_string = ''
row = 0
result = ''
for i in range(0, len(string2)):
    index_string_2 = string2[i]
    new_string = (new_string + index_string_2)
    for j in range(1, len(string1)):
        if j <= row:
            continue
            index_string = string1[j]
            old_str = (old_str + index_string)
        else:
            index_string = string1[j]
            old_str = (old_str + index_string)
    if not result == (new_string + old_str):
        print(new_string + old_str)
    result = (new_string + old_str)
    old_str = ''
    row += 1

