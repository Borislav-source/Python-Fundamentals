party_size = int(input())
days = int(input())
money = 0
expenses = 0
# malus = int
# bonus1 = (days // 3) * party_size * 3
# bonus2 = (days // 5) * party_size * 20
# if days % 3 == 0 and days % 5 == 0:
#     malus += 1
# money = (((days * 50) + bonus2) - ((days * 2 * party_size) + bonus1)) // party_size
# print(money)

for i in range(1, days + 1):
    money += 50
    if i % 10 == 0:
        party_size -= 2
    if i % 15 == 0:
        party_size += 5
    expenses += party_size * 2
    if i % 5 == 0:
        money += party_size * 20
    if i % 3 == 0:
        expenses += party_size * 3
    if i % 3 == 0 and i % 5 == 0:
        expenses += party_size * 2
result = (money - expenses) // party_size
print(f'{party_size} companions received {result} coins each.')

