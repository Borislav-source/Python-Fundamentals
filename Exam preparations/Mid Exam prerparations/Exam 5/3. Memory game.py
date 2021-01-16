elements = input().split()
moves = 0
condition = False

while True:
    data = input()
    if data == "end":
        break
    a, b = data.split()
    index1 = int(a)
    index2 = int(b)
    if not condition:
        moves += 1
        if 0 <= index1 < len(elements) > index2 >= 0 and not index1 == index2:
            if elements[index1] == elements[index2]:
                print(f"Congrats! You have found matching elements - {elements[index1]}!")
                elements = [el for el in elements if not el == elements[index1]]
            else:
                print("Try again!")
        else:
            half = len(elements) // 2
            elements = elements[:half] + [f"-{moves}a"] + [f"-{moves}a"] + elements[half:]
            print("Invalid input! Adding additional elements to the board")
    if len(elements) <= 0:
        condition = True
if condition:
    print(f"You have won in {moves} turns!")
else:
    print(f"Sorry you lose :(\n{' '.join(elements)}")

