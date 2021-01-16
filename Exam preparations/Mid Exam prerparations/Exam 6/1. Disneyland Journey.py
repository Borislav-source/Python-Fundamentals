journey_cost = float(input())
months = int(input())
savings = 0
for month in range(1, months + 1):
    if not month % 2 == 0 and month is not 1:savings *= 0.84
    elif month % 4 == 0:savings *= 1.25
    savings += journey_cost * 0.25
souvenirs_budget = abs(savings - journey_cost)
if savings >= journey_cost:print(f"Bravo! You can go to Disneyland and you will have {souvenirs_budget:.2f}lv. for souvenirs.")
else:print(f"Sorry. You need {souvenirs_budget:.2f}lv. more.")