
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):

    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):

    #create dictionary with unique value
    secretWordDict = {}
    for elt in secretWord: 
        secretWordDict[elt] = 0 
    #check if letters exists
    for elt in lettersGuessed:
        if elt in secretWordDict.keys():
            secretWordDict[elt]  += 1        
    #check dictionary if in dictionary is 0 then not compare
    for elt in secretWordDict.values():
        if elt == 0:
            return False
    return True
    

def getGuessedWord(secretWord, lettersGuessed):

    ans = []
    for letter in secretWord:
        if letter in lettersGuessed:
            ans.append(letter)
        else:
            ans.append(" _ ")
    return ''.join(ans)


def getAvailableLetters(lettersGuessed):
  
    # list with all alfabet letters
    alfabet = []
    for l in string.ascii_lowercase:
        alfabet.append(l)
    # remove existing letters from list  
    for i in lettersGuessed:
        if i in alfabet:    
            alfabet.remove(i)
    return ''.join(alfabet)


def hangman(secretWord):
    lettersGuessed1 = []
    lettersGuessed = []
    mistakesMade = 0
    print( "Welcome to the game, Hangman!" )
    print ( "I am thinking of a word that is " + str( len( secretWord ) ) + " letters long." )
   
    while True:
        print ( "-------------" )
        print ( "You have "+ str( 8 - mistakesMade ) + " guesses left." )
        print("Available letters: ", getAvailableLetters(lettersGuessed) )
        newLetter = input( "Please guess a letter: " ).lower()
        lettersGuessed.append( newLetter )
        if newLetter not in lettersGuessed1:
            lettersGuessed1.append(newLetter)
            if isWordGuessed(secretWord, lettersGuessed1):
                print( "Good guess: ", getGuessedWord(secretWord, lettersGuessed1) )
                print ( "-------------" )
                print( "Congratulations, you won!" )   
                break 
            else:
                if lettersGuessed[-1] in secretWord:
                    print( "Good guess: ", getGuessedWord(secretWord, lettersGuessed1) )                
                else:
                    print( "Oops! That letter is not in my word:", getGuessedWord( secretWord, lettersGuessed1) )
        else:
            print( "Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed1) )
            mistakesMade += 1
             
           
        if (8 - mistakesMade) == 0:
            print ( "-------------" )
            print( "Sorry, you ran out of guesses. The word was else. " )
            break    
#secretWord = chooseWord(wordlist).lower()
#hangman(secretWord)

secretWord = "sea"
hangman(secretWord)

#isWordGuessed(secretWord, lettersGuessed) #true false
#getGuessedWord(secretWord, lettersGuessed) #_ _ a _ 
#getAvailableLetters(lettersGuessed) #letter not gussed

#If aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0} then your function should return [1, 3, 8]
#If aDict = {1: 1, 2: 1, 3: 1} then your function should return []
    #aDict = { 1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0 }
    #aDict = {1: 1, 2: 1, 3: 1}

def uniqueValues(aDict):

    eDict = {}
    remeberDupKey = {}            
    for aKey, aValue in sorted( aDict.items() ):    
    
        if aValue in eDict.keys():
            remeberDupKey[aKey] = aValue   
        else:
            eDict[aValue] = aKey

    yDict = eDict.copy()

    for elt in remeberDupKey.values():
        if elt in yDict:
            del yDict[elt]  

    return(sorted(yDict.values()))

aDict = { 1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0 }
#aDict = {1: 1, 2: 1, 3: 1}
print( uniqueValues( aDict ) ) 

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    newL = []
    for i in L:
        if g(f(i)):
            newL.append(i)
    L[:] = newL
    if len(L) > 0:
        return max(L)
    else:
        return -1

def f(i):
    return i + 2
def g(i):
    return i > 5

L = [-1,-2,7,8]
print(applyF_filterG(L, f, g))
print(L)