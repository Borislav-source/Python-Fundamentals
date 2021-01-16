employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
people_count = int(input())
hours = 0
efficiency = employee1 + employee2 + employee3

while True:
    if people_count <= 0:
        break
    hours += 1
    if hours % 4 == 0:
        hours += 1
    people_count -= efficiency
print(f"Time needed: {hours}h.")
