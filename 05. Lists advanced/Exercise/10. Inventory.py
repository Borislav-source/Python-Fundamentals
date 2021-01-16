items = input().split(", ")
command = input()

while not command == 'Craft!':

    command = command.split(' - ')
    description = command[0]
    item = command[1]

    if description == 'Collect':
        if not item in items:
            items.append(item)
    elif description == 'Drop':
        if item in items:
            items.remove(item)
    elif description == 'Combine Items':
        item = item.split(':')
        old_item = item[0]
        new_item = item[1]
        [items.insert(ele + 1, new_item) for ele in range(len(items)) if old_item == items[ele]]
    elif description == 'Renew':
        if item in items:
            items.remove(item)
            items.append(item)
    command = input()
[print(items[position], end=', ') if not position == len(items) - 1 else print(items[position]) for position in range(len(items))]