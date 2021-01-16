sequence = list(map(int, input().split()))
while True:
    command = input()
    if command == "End":
        break
    command = int(command)
    for el in range(len(sequence)):
        if sequence[el] != None and el == command:
            for i in range(len(sequence)):
                if sequence[i] is not None and not i == el:
                    if sequence[i] > sequence[el]:
                        sequence[i] -= sequence[el]
                    else:
                        sequence[i] += sequence[el]
            sequence[el] = None
shot_targets = sequence.count(None)
sequence = [-1 if el is None else el for el in sequence]
print(f'Shot targets: {shot_targets} -> {" ".join(list(map(str, sequence)))}')
