number_of_loses = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
expenses = 0
k = 0
for i in range(1, number_of_loses + 1):
    if i % 2 == 0:
        expenses += helmet
    if i % 3 == 0:
        expenses += sword
    if i % 2 == 0 and i % 3 == 0:
        expenses += shield
        k += 1
        if k % 2 == 0:
            expenses += armor
print(f'Gladiator expenses: {expenses:.2f} aureus')
