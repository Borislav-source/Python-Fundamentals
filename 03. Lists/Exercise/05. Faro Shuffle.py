list_of_deck = input().split()
faroe_number = int(input())
list_one = []
list_two = []
result_list = []

half = len(list_of_deck) // 2
for k in range(faroe_number):
    for i in range(half):
        list_one.append(list_of_deck[i])
    for j in range(half, len(list_of_deck)):
        list_two.append(list_of_deck[j])
    list_of_deck.clear()
    for i in range(half):
        list_of_deck.append(list_one[i])
        list_of_deck.append(list_two[i])
    list_one.clear()
    list_two.clear()
print(list_of_deck)





