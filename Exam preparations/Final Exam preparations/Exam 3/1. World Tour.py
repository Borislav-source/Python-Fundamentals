stops = input()
data = input()

while not data == 'Travel':
    command, index, string = data.split(':')
    if command == 'Add Stop':
        index = int(index)
        if index in range(len(stops)):
            stops = stops[:index] + string + stops[index:]
        print(stops)
    elif command == 'Remove Stop':
        start = int(index)
        end = int(string)
        if start in range(len(stops)) and end in range(len(stops)):
            stops = stops[:start] + stops[end +1:]
        print(stops)
    elif command == 'Switch':
        old = index
        new = string
        if old in stops:
            stops = stops.replace(old, new)
        print(stops)
    data = input()
print(f"Ready for world tour! Planned stops: {stops}")