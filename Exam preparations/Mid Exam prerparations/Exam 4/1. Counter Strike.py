energy = int(input())
count = 0
condition = True
while True:
    distance = input()
    if distance == "End of battle":
        break
    distance = int(distance)
    if energy - distance < 0:
        print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
        condition = False
        break
    energy -= distance
    count += 1
    if count % 3 == 0:
        energy += count
if condition:
    print(f"Won battles: {count}. Energy left: {energy}")
