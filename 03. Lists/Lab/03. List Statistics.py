number_of_lines = int(input())
positive_list = []
negative_list = []
for i in range(0, number_of_lines):
    number = int(input())
    if number >= 0:
        positive_list.append(number)
    else:
        negative_list.append(number)
print(f'''{positive_list}
{negative_list}''')
print(f'Count of positives: {len(positive_list)}. '
      f'Sum of negatives: {sum(negative_list)}')
