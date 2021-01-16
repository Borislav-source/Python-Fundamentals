def swap(element, i, j):
    return ''.join((element[:i], element[j], element[i+1:j], element[i], element[j+1:]))


message = input().split()
for element in message:
    if 47 < ord(element[2]) < 58:
        element = (chr(int(element[:3])) + element[3:])
        if not len(element) > 2:
            print(element, end=' ')
        else:
            print(swap(element, 1, len(element) - 1), end=' ')
    else:
        element = (chr(int(element[:2])) + element[2:])
        if not len(element) > 2:
            print(element, end=' ')
        else:
            print(swap(element, 1, len(element) - 1), end=' ')
