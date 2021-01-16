new_pass = input()
data = input()


while not data == 'Done':
    data = data.split()
    if data[0] == 'TakeOdd':
        raw_pass = ''
        for char in range(len(new_pass)):
            if char % 2 != 0:
                raw_pass += new_pass[char]
        new_pass = raw_pass
        print(new_pass)
    elif data[0] == 'Cut':
        index = int(data[1])
        length = index + int(data[2])
        new_pass = new_pass[:index] + new_pass[length:]
        print(new_pass)
    elif data[0] == 'Substitute':
        substring = data[1]
        substitute = data[2]
        if substring in new_pass:
            new_pass = new_pass.replace(substring, substitute)
            print(new_pass)
        else:
            print('Nothing to replace!')
    data = input()
print(f'Your password is: {new_pass}')
