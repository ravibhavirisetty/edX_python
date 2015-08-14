# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Raviteja Bhavirisetty <ravi>
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "ps4_words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#

def getWordScore(word, n):
    score = 0
    if word == '':
        return 0
    else:
        for i in word:
            score += SCRABBLE_LETTER_VALUES[i]
    score *= len(word)
    if len(word) == n:
        return (score + 50)
    else:
        return score


#
# Problem #2: Make sure you understand how this function works and what it does!
#

def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#

def dealHand(n):
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#

def updateHand(hand, word):
    hand_copy = hand.copy()
    if word == '':
        return hand_copy
    else:
        for i in word:
            hand_copy[i] = hand_copy.get(i,0) - 1
        return hand_copy



#
# Problem #3: Test word validity
#

def isValidWord(word, hand, wordList):
    if word not in wordList:
        return False
    else:
        result = True
        hand_copy = hand.copy()
        for i in word:
            if i in hand_copy.keys() and hand_copy[i] > 0:
                result = result and True
                hand_copy[i] = hand_copy.get(i,0) - 1
            else:
                result = result and False
        return result


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    length = 0
    for i in hand.values():
        length += i
    return length



def playHand(hand, wordList, n):
    total_score = 0
    while sum(hand.values()) > 0:
        print 'Current hand:',
        displayHand(hand)
        hand_copy = hand.copy()
        guess = raw_input('Enter word, or a "." to indicate that you are finished: ')
        if guess == '.':
            print 'Goodbye! Total score:', total_score, 'points.\n'
            break
        else:
            if isValidWord(guess, hand, wordList):
                total_score += getWordScore(guess, n)
                print '\"' + guess + '\"' , 'earned', getWordScore(guess, n), 'points. Total:', total_score, 'points'
                hand = updateHand(hand, guess)
                print ''
            else:
                print 'Invalid word, please try again.'
                print ''
    if sum(hand.values()) == 0:
        print 'Ran out of letters. Total score:', total_score, 'points.'



#
# Problem #5: Playing a game
# 

def playGame(wordList):
    hand = ''
    while True:
        command = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if command == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        elif command == 'r':
            if hand == '':
                print 'You have not played a hand yet. Please play a new hand first!'
                print ''
            else:
                playHand(hand, wordList, HAND_SIZE)
        elif command == 'e':
            break
        else:
            print 'Invalid command.'

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
