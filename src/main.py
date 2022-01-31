import tkinter
import parse
word_pron = parse.word_pron
rhyme_groups = parse.rhyme_groups

def check_rhyme(word_1, word_2, req):
    if word_1.upper() in word_pron:
        first_sounds = word_pron[word_1.upper()][-req:]
    else:
        return False
    if word_2.upper() in word_pron:
        second_sounds = word_pron[word_2.upper()][-req:]
    else:
        return False

    return first_sounds == second_sounds

def main():
    parse.main()
    word1 = input('Enter the first word: ')
    word2 = input('Enter the second word: ')
    req = input('Syllable requirement: ')
    print( 'Rhyme' if check_rhyme(word1, word2, int(req)) else 'Not a rhyme')
    return 0

if __name__ == '__main__':
    main()