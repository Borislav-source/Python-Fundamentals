first_sentence = input()
second_sentence = input()
last = ''
for i in range(1, len(first_sentence) + 1):
    result = second_sentence[:i] + first_sentence[i:]
    if first_sentence != result != last:
        print(result)
    last = result
