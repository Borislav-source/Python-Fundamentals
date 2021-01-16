data = input()
company_dict = {}
while not data == 'End':
    company_name, employee = data.split(" -> ")
    if company_name not in company_dict:
        company_dict[company_name] = []
    if employee not in company_dict[company_name]:
        company_dict[company_name].append(employee)
    data = input()
sorted_dict = dict(sorted(company_dict.items()))
for key in sorted_dict:
    print(key)
    for index in range(len(sorted_dict[key])):
        print(f'-- {sorted_dict[key][index]}')
