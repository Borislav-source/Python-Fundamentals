message = input()
data = input()

while not data == 'Reveal':
    data = data.split(":|:")
    command = data[0]
    if command == 'InsertSpace':
        index = int(data[1])
        message = message[:index] + ' ' + message[index:]
        print(message)

    elif command == 'Reverse':
        substring = data[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            message += substring[::-1]
            print(message)
        else:
            print('error')
    elif command == 'ChangeAll':
        substring = data[1]
        replacement = data[2]
        message = message.replace(substring, replacement)
        print(message)
    data = input()
print(f'You have a new text message: {message}')