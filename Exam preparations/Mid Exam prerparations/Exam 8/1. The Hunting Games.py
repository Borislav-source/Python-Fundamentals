days = int(input())
players_count = int(input())
energy = float(input())
water_for_one = float(input())
food_for_one = float(input())
water = days * water_for_one * players_count
food = days * food_for_one * players_count
condition = True
for day in range(1, days + 1):
    energy_loss = float(input())
    energy -= energy_loss
    if energy <= 0:
        condition = False
        break
    if day % 2 == 0:
        water *= 0.7
        energy *= 1.05
    if day % 3 == 0:
        food -= food / players_count
        energy *= 1.10
if condition:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food:.2f} food and {water:.2f} water.")
