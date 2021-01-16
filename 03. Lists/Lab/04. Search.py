num = int(input())
key_word = input()
list_of_sentences = list()
other_list_of_sentences = list()

for i in range(num):
    sentence = input()
    list_of_sentences.append(sentence)
for k in range(0, num):
    if key_word in list_of_sentences[k]:
        other_list_of_sentences.append(list_of_sentences[k])
print(f'''{list_of_sentences}
{other_list_of_sentences}''')