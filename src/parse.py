import re

dict = open('data/cmudict-07b')
word_pron = {}

def read():
    lines = dict.readlines()
    for line in lines:
        parts = line.split(' ')
        word = parts[0]
        print(word)
        if(word.strip() != ';;;'):
            sounds = parts[2:]
            word_pron[word] = sounds


def main():
    read()


if __name__ == '__main__':
    main()