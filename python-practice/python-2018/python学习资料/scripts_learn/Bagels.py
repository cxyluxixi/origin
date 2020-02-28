import random
def getSecretNum(numDigits):
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return ' You got it.'
    clue = []
    for i in range(len(guess)):
        if guess[i]==secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
    if len(clue) == 0:
        return 'Bagels'
    clue.sort()
    return ' '.join(clue)

def isOnlyDigits(num):
    if num== '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9':
            return False

    return True

def playAgain():
    print('do you want to play again?')
    return input().lower().startswith('y')
NUMDIGITS = 3
MAXGUESS = 10



while True:
    secretNum = getSecretNum(NUMDIGITS)
    print('I have a number, Please guess.')
    numGuesses = 1
    while numGuesses <= MAXGUESS:
        guess = ''
        while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
            print('Guess #%s :' % (numGuesses))
            guess = input()

        clue = getClues(guess, secretNum)
        print(clue)
        numGuesses +=1

        if guess ==secretNum :
            break
        if numGuesses > MAXGUESS:
            print('You lost.')

    if not playAgain():
        break
