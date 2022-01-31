
dict = open('data/cmudict-07b')
word_pron = {}
rhyme_groups = {}

rhyme_requirement = 2

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

def construct_file():
    f = open('out/rhymegroups.txt', 'w')
    for group in rhyme_groups:
        words = rhyme_groups[group]
        f.write(str(group) + ': ')
        for word in words:
            f.write(word + " ")
        f.write('\n')

def construct_rhyme_groups():
    for word in word_pron:
        last_sounds = tuple(word_pron[word][-rhyme_requirement:])
        if not last_sounds in rhyme_groups:
            rhyme_groups[last_sounds] = list()
        rhyme_groups[last_sounds].append(word)

def main():
    read()
    construct_rhyme_groups()
    # construct_file()

def get_word_pron():
    read()
    return word_pron


if __name__ == '__main__':
    main()
    dict.close()