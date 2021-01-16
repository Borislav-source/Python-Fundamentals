rows = int(input())
my_dict = {}
for row in range(rows):
    name = input()
    grade = float(input())
    if name not in my_dict:
        my_dict[name] = []
    my_dict[name].append(grade)
for name in my_dict:
    my_dict[name] = round(sum(my_dict[name]) / len(my_dict[name]), 2)
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
for key in sorted_dict:
    if 6 >= sorted_dict[key] >= 4.50:
        print(f"{key} -> {sorted_dict[key]:.2f}")