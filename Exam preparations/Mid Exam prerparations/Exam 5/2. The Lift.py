people_count = int(input())
lifts = list(map(int, input().split()))

for el in range(len(lifts)):
    people = lifts[el]
    if people < 4 and people_count > 0:
        loading = 4 - people
        if people_count - loading >= 0:
            people_count -= loading
            lifts[el] += loading
        else:
            lifts[el] = people_count
            people_count = 0
if people_count == 0 and len(lifts) == lifts.count(4):
    print(" ".join(list(map(str, lifts))))
elif people_count == 0:
    print(f'''The lift has empty spots!
{" ".join(list(map(str, lifts)))}
''')
elif people_count > 0:
    print(f'''There isn't enough space! {people_count} people in a queue!
{" ".join(list(map(str, lifts)))}
''')
