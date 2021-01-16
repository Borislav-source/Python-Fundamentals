import re
text = input()
pattern = r"(#|\|)(?P<food>[A-Z a-z]+)(\1)(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})(\1)(?P<cal>\d+)(\1)"
provisions = re.finditer(pattern, text)
my_list = []
cals = 0
for day in provisions:
    my_list.append(f"Item: {day.group('food')}, Best before: {day.group('date')}, Nutrition: {day.group('cal')}")
    cals += int(day.group('cal'))
days = cals // 2000
print(f"You have food to last you for: {days} days!")
for p in my_list:
    print(p)
