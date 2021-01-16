data = input()
my_dict = {}
while not data == 'end':
    course, student = data.split(" : ")
    if course not in my_dict:
        my_dict[course] = [student]
    else:
        my_dict[course].append(student)
    my_dict[course] = sorted(my_dict[course])
    data = input()
sorted_dict = sorted(my_dict, key=lambda k: len(my_dict[k]), reverse=True)

for key in sorted_dict:
    print(f'{key}: {len(my_dict[key])}')
    for name in range(len(my_dict[key])):
        print(f'-- {my_dict[key][name]}')