#file = open("sample.txt")
with open('sample.txt') as f:
    file = str(f)

import re
import operator


def count_words(file):
    """This will count the words and print in a (word, count) format."""
    words = {}
    file = file.lower()
    file = file.split()
    for word in file:
        word = re.sub(r'[^A-Za-z0-9]',"", word)
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    for word, count in sorted(words.items(), key=operator.itemgetter(1), reverse=True):
        top_words = sorted(words.items(), key=lambda x: (count, word))[:]
    for word, count in top_words:
        print(word, count)



count_words(file)
