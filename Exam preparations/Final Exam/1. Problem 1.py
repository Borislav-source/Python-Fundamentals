text = input()
data = input()
while not data == 'Done':
    data = data.split()
    command = data[0]
    if command == 'Change':
        char = data[1]
        replacement = data[2]
        text = text.replace(char, replacement)
        print(text)
    elif command == 'Includes':
        other_string = data[1]
        check = bool(other_string in text)
        print(check)
    elif command == 'End':
        string = data[1]
        check = text.endswith(string)
        print(check)
    elif command == 'Uppercase':
        text = text.upper()
        print(text)
    elif command == 'FindIndex':
        char = data[1]
        for el in range(len(text)):
            if text[el] == char:
                print(el)
                break
    elif command == 'Cut':
        start = int(data[1])
        end = int(data[2])
        text = text[start:end + start]
        print(text)
    data = input()
