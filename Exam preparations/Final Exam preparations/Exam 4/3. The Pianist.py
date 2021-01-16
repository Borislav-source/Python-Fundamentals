from collections import OrderedDict
from operator import getitem
number_of_pieces = int(input())
pianists_dict = {}
for _ in range(number_of_pieces):
    piece, composer, key = input().split('|')
    if key not in pianists_dict:
        pianists_dict[key] = {}
    if composer not in pianists_dict[key]:
        pianists_dict[key][composer] = []
    pianists_dict[key][composer].append(piece)
data = input()
while not data == 'Stop':
    data = data.split('|')
    command, piece = data[:2]
    if command == 'Add':
        composer, key = data[2:]
        if key in pianists_dict:
            if composer in pianists_dict[key]:
                for k in pianists_dict:
                    if piece in pianists_dict[k][composer]:
                        print(f"{piece} is already in the collection!")
                        break
                else:
                    pianists_dict[key][composer].append(piece)
            else:
                pianists_dict[key][composer] = []
                pianists_dict[key][composer].append(piece)
                print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            pianists_dict[key] = {}
            pianists_dict[key][composer] = []
            pianists_dict[key][composer].append(piece)
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command == 'Remove':
        condition = False
        for key in pianists_dict:
            for composer in pianists_dict[key]:
                if piece in pianists_dict[key][composer]:
                    pianists_dict[key][composer].remove(piece)
                    print(f"Successfully removed {piece}!")
                    condition = True
                    if len(pianists_dict[key][composer]) <= 0:
                        del pianists_dict[key][composer]
                    break
            if condition:
                break
        if not condition:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command == 'ChangeKey':
        new_key = data[2]
        condition = False
        for key in pianists_dict:
            for composer in pianists_dict[key]:
                if piece in pianists_dict[key][composer] and not key == new_key:
                    pianists_dict[key][composer].remove(piece)
                    if len(pianists_dict[key][composer]) <= 0:
                        del pianists_dict[key][composer]
                    condition = True
                    cmp = composer
                    print(f"Changed the key of {piece} to {new_key}!")
                    break
            if condition:
                break
        if condition:
            if new_key in pianists_dict:
                for i in pianists_dict[new_key]:
                    if cmp in pianists_dict[new_key]:
                        pianists_dict[new_key][cmp].append(piece)
                else:
                    pianists_dict[new_key][cmp] = []
                    pianists_dict[new_key][cmp].append(piece)
            else:
                pianists_dict[new_key] = {}
                pianists_dict[new_key][cmp] = []
                pianists_dict[new_key][cmp].append(piece)
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    data = input()
my_list = []
for key in pianists_dict:
    for com in pianists_dict[key]:
        my_list.extend(pianists_dict[key][com])
for i in sorted(my_list):
    for key in pianists_dict:
        for com in pianists_dict[key]:
            if i in pianists_dict[key][com]:
                print(f"{i} -> Composer: {com}, Key: {key}")