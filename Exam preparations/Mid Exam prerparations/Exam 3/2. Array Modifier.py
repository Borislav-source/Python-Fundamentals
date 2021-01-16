array_of_integers = list(map(int, input().split(" ")))

while True:
    data = input()
    if data == "end":
        break
    command = data.split()[0]

    if command == "swap":
        index1 = int(data.split()[1])
        index2 = int(data.split()[2])
        array_of_integers[index1], array_of_integers[index2] = array_of_integers[index2], array_of_integers[index1]
    elif command == "multiply":
        index1 = int(data.split()[1])
        index2 = int(data.split()[2])
        array_of_integers[index1] *= array_of_integers[index2]
        # array_of_integers.remove(array_of_integers[index2])
    elif command == "decrease":
        array_of_integers = [array_of_integers[el] - 1 for el in range(len(array_of_integers))]
print(", ".join(list(map(str, array_of_integers))))

