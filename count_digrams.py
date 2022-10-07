import sys
from collections import Counter
import load_dictionary

def main():
    word = 'voldemort'

    #load words from dictionary
    dict_file = load_dictionary.load('2of4brif.txt')

    #find digrams in 'voldemort'
    digrams = set()
    for i in range(len(word)):
        for j in range(len(word)):
            if i != j:
                this_digram = word[i] + word[j]
                digrams.add(this_digram)

    print(digrams)
    print("Number of digrams is: {}".format(len(digrams)))

    #count frequency of occurrence of digrams in dictionary file
    frequency_list = []
    for word in dict_file:
        for digram in digrams:
            for i in range(len(word) - 1):
                if word[i:i+2] == digram:
                    frequency_list.append(digram)

    digram_count = Counter(frequency_list)

    print(digram_count)


if __name__ == '__main__':
    main()