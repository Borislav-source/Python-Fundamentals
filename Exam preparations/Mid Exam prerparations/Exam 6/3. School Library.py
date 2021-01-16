shelf = input().split('&')
data = input()
while not data == "Done":
    command, book_name, *book2 = data.split(' | ')
    if command == "Add Book":
        if book_name not in shelf:
            shelf.insert(0, book_name)
    elif command == "Take Book":
        if book_name in shelf:
            shelf.remove(book_name)
    elif command == "Swap Books":
        book2 = ''.join(book2)
        if book_name in shelf and book2 in shelf:
            for book in range(len(shelf)):
                if shelf[book] == book_name:shelf[book] = book2
                elif shelf[book] == book2:shelf[book] = book_name
    elif command == 'Insert Book':
        shelf.append(book_name)
    elif command == 'Check Book':
        index = int(book_name)
        if index in range(len(shelf)):
            print(shelf[index])
    data = input()
print(', '.join(shelf))
