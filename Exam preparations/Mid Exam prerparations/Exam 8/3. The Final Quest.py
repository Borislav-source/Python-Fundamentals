words_collection = input().split()
data = input()
while not data == 'Stop':
    data = data.split()
    command = data[0]
    if command == 'Delete':
        index = int(data[1]) + 1
        if index in range(len(words_collection)):
            words_collection.remove(words_collection[index])
    elif command == 'Swap':
        word1 = data[1]
        word2 = data[2]
        if word1 in words_collection and word2 in words_collection:
            for ind in range(len(words_collection)):
                if words_collection[ind] == word1:words_collection[ind] = word2
                elif words_collection[ind] == word2:words_collection[ind] = word1
    elif command == 'Put':
        word1 = data[1]
        index = int(data[2]) - 1
        if index in range(len(words_collection)):
            words_collection.insert(index, word1)
        elif index == len(words_collection):
            words_collection.append(word1)
    elif command == 'Sort':
        words_collection.sort(reverse=True)
    elif command == 'Replace':
        word1 = data[1]
        word2 = data[2]
        if word2 in words_collection:
            for i in range(len(words_collection)):
                if words_collection[i] == word2:
                    words_collection[i] = word1
                    break
    data = input()
print(' '.join(words_collection))
