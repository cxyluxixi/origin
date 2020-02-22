import random
import sys

def drawBoard(board):
    hline = '    '
    for i in range(1,6):
        hline += (' '*9) + str(i)
    print(hline)
    print('   ' + ('0123456789' * 6))
    print()

    for i in range(15):
        if i <10:
            extraSpace = ' '
        else:
            extraSpace = ''
        print('%s%s %s %s' % (extraSpace, i ,getRow(board, i), i ))

    print()
    print('   '+('0123456789'*6))
    print(hline)

    
def getRow(board, row):
    boardRow = ''
    for i in range(60):
        boardRow += board[i][row]
    return boardRow

def getNewBoard():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0,1)==0:
                board[x].append('~')
            else:
                board[x].append('`')

        return board

def getRandomChests(numChests):
    chests = []
    for i in range(numChests):
        chests.append([random.randint(0,59),random.randint(0,14)])
    return chests

def isValidMove(x, y):
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def makeMove(board, chests,x,y):
    if not isValidMove(x,y):
        return False
    smallestDistance = 100
    for cx,cy in chests:
        if abs(cx - x ) > abs(cy -y):
            distance = abs(cx - x)
        else:
            distance = abs(cy - y)
        if distance < smallestDistance :
            smallestDistance = distance

    if smallestDistance == 0:
        chests.remove([x,y])
        return 'You have found a sunken treasure chest!'
    else:
        if smallestDistance <10:
            board[x][y] = str(smallestDistance)
            return 'Treasure detected at a distance of %s from the somar device.' % (smallestDistance)
        else:
            board[x][y] = '0'
            return 'Sonar did not detect anything. All treasure chests out of range.'

def enterPlayerMove():
    print('Where do you want to drop the next sonar device?(0-59 0-14) (or type quit)')
    while True:
        move = input()
        if move.lower()=='quit':
            print('Thanks for playing!')
            sys.exit()

        move = move.split()
        if len(move) ==2 and move[0].isdigit()and move[1].isdigit()and isValidMove(int(move[0]), int(move[1])):
            return [int(move[1]),int(move[1])]
        print ('Enter a number from 0 to 59,a space ,then a number from 0 to 14.')


def playAgain():
    print('Do you want to paly again?(yes or no)')
    return input().lower.startswith('y')

def showInstructions():
     print('''Instructions:..................
.................''')
     input()
     print('''For example ,here is a treasure chest(the c) located a distance of 2 away
from the sonar device(the d ):
    22222
    c   2
    2 d 2
    2   2
    22222

The point where the device was dropped will be marked with a 2.

The treasure............''')
     input()
     print()

print('S O N A R!')
print()
print('Would you like to view the instructions?(yes/no)')
if input().lower().startswith('y'):
    showInstructions()

while True:
    sonarDevices = 16
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    previousMoves = []
    while sonarDevice > 0:
        if sonarDevice > 1:
            extraSsonar = 's'
        else:
            extraSsonar = ''
        if len(theChests) > 1:
            extraSchest = 's'
        else:
            etraSchest =''
        print('You have %s sonar device%s left. %s treasure chest %s remaining.' % (sonarDevice, extraSsonar,len(theChests),extraSchest))

        x, y = enterPlayerMove()
        previousMoves.append([x,y])
        moveResult = makeMove(theBoard, theChests, x, y )
        if moveResult ==False :
            continue
        else:
            if moveResult == 'You have found a sunken treasure chest!':
                for x, y in previousMoves:
                    makeMove(theBoard,theChests,x, y )

            drawBoard(theBoard)
            print(moveResult)

        if len(theCHests) == 0:
            print('You have found all the sunken treasure chests! Congratulations and good game')
            break
        sonarDevice  -=1

    if sonarDevice == 0:
        print ('we\'ve run out of sonar devices! Now we have to turn the ship around and head')
        print ('for home with treasure chests still out there. Game over')
        print ('  the remaining chests were there :')
        for x,y in theChests:
            print('   %s ,%s' %(x,y))

    if not playAgain():
        sys.exit()
        

    
                  
     
