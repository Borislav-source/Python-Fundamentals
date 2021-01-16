exam_dict = {}
points_dict = {}
banned = []
data = input()
while not data == 'exam finished':
    data = data.split('-')
    username = data[0]
    if len(data) == 3:
        language = data[1]
        points = int(data[2])
        if language not in exam_dict:
            exam_dict[language] = []
        exam_dict[language].append(username)
        if username not in points_dict:
            points_dict[username] = []
        points_dict[username].append(points)
    if len(data) == 2:
        if username not in banned:
            banned.append(username)
    data = input()
print('Results:')
for key in dict(sorted(points_dict.items(), key= lambda x: (-max(x[1]), x[0]))):
    if key not in banned:
        print(f'{key} | {max(points_dict[key])}')
print('Submissions:')
for key in dict(sorted(exam_dict.items(), key= lambda x: (-len(x[1]), x[0]))):
    print(f'{key} - {len(exam_dict[key])}')
