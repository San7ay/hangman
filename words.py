""" Function to fetch word depending on the difficulty level """

import random

WORDLIST = 'wordDatabase.txt'


def get_word(difficulty_level):
    """Get a random word from the list considering the difficulty level"""
    """ Difficulty level      word length range
        EASY                   4-7 
        MEDIUM                 8-11
        DIFFICULT              12-15 """
    possible_words_list = []
    word_size = 0

    """Select a random word size within the difficulty level defined"""
    if difficulty_level == '1':
        word_size = random.randint(4, 7)
    elif difficulty_level == '2':
        word_size = random.randint(8, 11)
    elif difficulty_level == '3':
        word_size = random.randint(12, 15)

    """Select each word, format and add to possible word list if agreed upon"""
    with open(WORDLIST, 'r') as f:
        for word in f:
            if '(' in word or ')' in word:
                continue
            """remove whitespace at the end and convert all letters to lowercase"""
            word = word.strip().lower()
            if len(word) == word_size:
                possible_words_list.append(word)        # select the word with required length

    """select random word from possible word list"""
    return random.choice(possible_words_list)
