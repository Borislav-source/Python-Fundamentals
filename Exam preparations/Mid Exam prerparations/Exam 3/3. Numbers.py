def average(sequence):
    return sum(sequence) / len(sequence)


sequence = list(map(int, input().split()))
avg = average(sequence)
result = [el for el in sequence if el > avg]
result = list(sorted(result, reverse=True))
if len(result) > 0:
    print(" ".join(list(map(str, result[:5]))))
else:
    print("No")
