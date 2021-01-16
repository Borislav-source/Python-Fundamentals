def maxBonus(stud_attendances, stud_count, lect_count, additional_bonus):
    result = stud_attendances / lect_count * (5 + additional_bonus)
    return round(result)


stud_count = int(input())
lect_count = int(input())
additional_bonus = int(input())
initial_bonus = 0
attendaces = 0


for student in range(stud_count):
    stud_attendances = int(input())
    data = maxBonus(stud_attendances, stud_count, lect_count, additional_bonus)
    if data > initial_bonus:
        initial_bonus = data
        attendaces = stud_attendances

print(f"Max Bonus: {initial_bonus}.\nThe student has attended {attendaces} lectures.")