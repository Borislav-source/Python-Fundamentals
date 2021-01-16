def count(element):
    count_item = 0
    for i in str(element):
        count_item += int(i)
    return count_item


nums = input().split()
sentence = input()

for element in nums:
    value = count(element)
    if value > len(sentence):
        value -= len(sentence)
        print(sentence[value], end="")
        sentence = sentence[:value] + sentence[value + 1:]
    else:
        print(sentence[value], end='')
        sentence = sentence[:value] + sentence[value + 1:]
