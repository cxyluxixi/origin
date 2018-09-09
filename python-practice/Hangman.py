import random
M = ['1','2','4','5','6','7']
words = 'ant bear cat dog fox grog goat lion monkey mouse panda snake'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0,len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(M, missedLetters,correctLetters,secretWord):
    print(M[len(missedLetters)])
    print()

    print('Missed letters:', end = ' ')
    for letter in missedLetters:
        print(letter, end = ' ')
    print()

    blanks = '_'*len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter , end = ' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    print('Do you want to play again?(yes or no)')
    return input().lower().startswith('y')


print(' HANGMAN')
missedLetters = ''
correctLetters =''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(M, missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes. The secret word is "' +secretWord +'"! You have won!')
            gameIsDone  = True

    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(M) - 1:
            displayBoard(M, missedLetters ,CorrectLetters, secretWord)
            print('You have run out of guesses.')
            gameIsDone =True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
        
