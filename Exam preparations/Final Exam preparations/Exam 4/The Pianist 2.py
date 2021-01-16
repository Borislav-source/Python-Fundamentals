number_of_pieces = int(input())
pianists_dict = {}
for _ in range(number_of_pieces):
    piece, composer, key = input().split('|')
    if piece not in pianists_dict:
        pianists_dict[piece] = [composer, key]
data = input()
while not data == 'Stop':
    data = data.split('|')
    command, piece = data[:2]
    if command == 'Add':
        composer, key = data[2:]
        if piece in pianists_dict:
            print(f"{piece} is already in the collection!")
        else:
            pianists_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command == 'Remove':
        if piece in pianists_dict:
            del pianists_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command == 'ChangeKey':
        new_key = data[2]
        if piece in pianists_dict:
            pianists_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    data = input()
for p in dict(sorted(pianists_dict.items(), key= lambda x: (x[0], x[1][0]))):
    print(f"{p} -> Composer: {pianists_dict[p][0]}, Key: {pianists_dict[p][1]}")
