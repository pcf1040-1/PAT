import re

dict = open('data/cmudict-07b')
word_pron = {}

rhyme_requirement = 3

def read():
    lines = dict.readlines()
    for line in lines:
        parts = line.split(' ')
        word = parts[0]
        if(word.strip() != ';;;'):
            sounds = parts[2:]
            word_pron[word] = sounds


def rhymes(parts_one : list, parts_two: list):
    first_len = len(parts_one)
    second_len = len(parts_two)
    first_parts = parts_one.copy()
    second_parts = parts_two.copy()
    first_parts.reverse(), second_parts.reverse()

    rhyme_count = 0

    for i in range(min(first_len, second_len)):
        if(first_parts[i] == second_parts[i]):
            rhyme_count += 1
        else:
            break

    if(rhyme_count >= rhyme_requirement):
        return True
    return False

def construct():
    f = open('out/adjList.txt', 'w')
    for word in word_pron:
        f.write(str(word) + ': ')
        for other_word in word_pron:
             if word != other_word:
                if rhymes(word_pron[word], word_pron[other_word]):
                    f.write(str(other_word) + ' ')
        f.write('\n')


def main():
    read()
    construct()


if __name__ == '__main__':
    main()
    dict.close()