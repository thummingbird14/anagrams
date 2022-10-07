import sys
from collections import Counter
import load_dictionary

def main():
    word = 'tmvoordle'

    #load words from dictionary
    dict_file = load_dictionary.load('2of4brif.txt')

    #find digrams in 'tmvoordle'
    digrams = set()
    for i in range(len(word)):
        for j in range(len(word)):
            if i != j:
                this_digram = word[i] + word[j]
                digrams.add(this_digram)

    print(digrams)
    print("Number of digrams is: {}".format(len(digrams)))

    #count frequency of occurrence of digrams in dictionary file
    #to use Counter need a list e.g ['de', 'dl', 'dm', 'de']
    #can't use 'for digram in word' because this won't work with volvo 


if __name__ == '__main__':
    main()