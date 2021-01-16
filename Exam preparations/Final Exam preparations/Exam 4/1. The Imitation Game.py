message = input()
data = input()

while not data == 'Decode':
    data = data.split('|')
    command = data[0]
    if command == 'Move':
        num_of_letters = int(data[1])
        sub = message[:num_of_letters]
        message = message[num_of_letters:]
        message += sub
    elif command == 'Insert':
        index = int(data[1])
        value = data[2]
        message = message[:index] + value + message[index:]

    elif command == 'ChangeAll':
        substring, replacement = data[1:]
        message = message.replace(substring, replacement)

    data = input()
print(f"The decrypted message is: {message}")