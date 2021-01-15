import random

def start():
    global board
    board = [
        ['7','8','9'],
        ['4','5','6'],
        ['1','2','3']
    ]

def printBoard():
    print('\n=============')
    for row in board:
        print('|', row[0], '|', row[1], '|', row[2], '|')
        print('=============')

def chooseOnePlayer():
    num = ''
    while(True):
        try: num = input('1 or 2 players?: ')
        except: print('\nEnter 1 or 2! ')

        if(num == '1'): 
            return True
        elif(num == '2'): 
            return False
        else: 
            print('\nEnter 1 or 2! ')

def getEmptySpots():
    spots = []
    for i in range(0, 3):
        for j in range(0, 3):
            if ( board[i][j] != 'X' and board[i][j] != 'O' ):
                spots.append(board[i][j])
    return spots

def placePiece(spot, piece):
    for i in range(0, 3):
        for j in range(0, 3):
            if (board[i][j] == spot):
                board[i][j] = piece

def getUserMove():
    spot = ''
    while(True):
        try: spot = input('Enter spot: ')
        except: print('\nEnter the number of the spot.')
        if (spot in getEmptySpots()): break
        else: print('\nEnter the number of the spot.')
    return spot

def checkWin():
    #Rows
    for i in range(0,3):
        if board[i][0] == board[i][1] == board[i][2]:
            printBoard()
            print(f"{board[i][0]}'s won!")
            return True
    #Columns
    for i in range(0,3):
        if board[0][i] == board[1][i] == board[2][i]:
            printBoard()
            print(f"{board[0][i]}'s won!")
            return True
    # Diagnols
    if board[0][0] == board[1][1] == board[2][2]:
        printBoard()
        print(f"{board[0][i]}'s won!")
        return True
    elif board[0][2] == board[1][1] == board[2][0]:
        printBoard()
        print(f"{board[0][i]}'s won!")
        return True

    # Stalemate
    if (len(getEmptySpots()) < 1):
        printBoard()
        print("Stalemate, no one wins!")
        return True

    # Return False
    else:
        return False

while(True):
    ## Initialize Board
    start()
    print()

    ## Step 1: Ask 2-player or 1-player
    onePlayer = chooseOnePlayer()

    ## Step 2: In Game - User input 1-9
    inGame = True
    while(inGame):

        # Player 1 moves
        printBoard()
        placePiece(getUserMove(), 'X')
        if (checkWin()): break
        
        # Player 2 moves
        if(not onePlayer):
            printBoard()
            placePiece(getUserMove(), 'O')
        else:
            placePiece( random.choice(getEmptySpots()), 'O' )
        if (checkWin()): break

    ## Step 3: End game - ask to replay, switch to 1/2 player, or quit
    print()
    answer = ''
    while(True):
        try: answer = input("Play again? (Y/N): ")
        except: print("\nEnter 'Y' for yes or 'N' for no.")
        if (answer.lower() == 'y' or answer.lower() == 'n'): break
        elif (answer.lower() == '1' or answer.lower() == '0'): break
        else: print("\nEnter 'Y' for yes or 'N' for no.")
    
    if( answer.lower() == 'n' ): break
    if( answer == '0' ): break