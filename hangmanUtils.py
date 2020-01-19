import string
import words

"""
Use index to display guessed letters in the word:
if the letter is guessed index = True
else index = False
"""


def get_display_word(strword, index):
    """check if the index is true and display the corresponding letter"""
    finalword = []
    word = [char for char in strword]               # convert string to list of letters
    if len(word) != len(index):
        raise ValueError('word length and indices length not same')
    for x in index:
        for y in word:
            if x:
                finalword.append(y)
            else:
                finalword.append('$')
            word.remove(y)
            break

    return ''.join([str(elem) for elem in finalword]).strip()


def get_next_letter(remaining_chance, unused_letter):
    """get the user inputed next letter"""
    if remaining_chance == 0:
        raise ValueError('You run out of chances')
    while True:
        next_letter = input('choose a letter: ').lower()
        if len(next_letter) != 1:
            print('{0} is not a single character'.format(next_letter))
        elif next_letter not in string.ascii_lowercase:
            print('{0} is not a letter'.format(next_letter))
        elif next_letter not in unused_letter:
            print('{0} has been guessed before'.format(next_letter))
        else:
            unused_letter.remove(next_letter)
            return next_letter


def play_hangman():
    print('Welcome to hangman game!! Try not to be hanged')
    level = input('Select the required difficulty level\n(1) EASY \n(2) MEDIUM\n(3) DIFFICULT\n')

    word = words.get_word(level)
    # print(word)              uncomment to know the word selected for testing
    """Initially set 'False' to all the letter in the word ....list show be same size as word length"""
    index = [letter not in string.ascii_lowercase for letter in word]
    remaining_letters = set(string.ascii_lowercase)
    wrong_letters = []
    word_solved = False
    number_of_attempts = len(word)  # choose num of attempts as num of letter in word

    while number_of_attempts > 0 and not word_solved:
        print('Word: {0}'.format(get_display_word(word, index)))
        print('Attempts remaining: {0}'.format(number_of_attempts))

        next_letter = get_next_letter(number_of_attempts,remaining_letters)

        if next_letter in word:
            print('{0} is in the word'.format(next_letter))
            for i in range(len(word)):
                if word[i] == next_letter:
                    index[i] = True
        else:
            print('{0} is NOT in the word'.format(next_letter))

        number_of_attempts -= 1
        wrong_letters.append(next_letter)

        if False not in index:
            word_solved = True
        print()

    print('"{0}" is the word'.format(word))

    if word_solved:
        print('Congrats!! you won')
    else:
        print('Better luck next time')

    tryagain = input('would you like to play again? [y/n]')
    return tryagain.lower() == 'y'


