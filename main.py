# Global variables
gb = dict() # gameboard = {'11':' ', '12':' ', ...}


# Assigns space to each position on board
def setgameboard():
    for i in range(4):
        for j in range(4):
            s = str(i)+str(j)
            gb[s] = ' '


def draw():
    '''
    draws the board based on the dictionary gameboard
    '''

    for i in range(3):
        for j in range(3):
            rc = str(i+1) + str(j+1) # rowcolumn string
            print("[{}]".format(gb[rc]), end ='')
        print()


def guide():
    '''
    To tell the user how to enter rows and columns
    '''

    print("The rows and columns are mentioned as [row,column]")
    for i in range(3):
        for j in range(3):
            print("[{}]".format(str(i + 1) + str(j + 1)), end='')
        print()


def check():
    '''
    To check the conditions of which the game can be won, lost or tied
    '''

    if ' ' not in list(gb.values()):
        return "Game Tied"
    elif gb['11'] == gb['12'] == gb['13'] != ' ':
        return "Won"
    elif gb['21'] == gb['22'] == gb['23'] != ' ':
        return "Won"
    elif gb['31'] == gb['32'] == gb['33'] != ' ':
        return "Won"
    elif gb['11'] == gb['21'] == gb['31'] != ' ':
        return "Won"
    elif gb['12'] == gb['22'] == gb['32'] != ' ':
        return "Won"
    elif gb['13'] == gb['23'] == gb['33'] != ' ':
        return "Won"
    elif gb['11'] == gb['22'] == gb['33'] != ' ':
        return "Won"
    elif gb['13'] == gb['22'] == gb['31'] != ' ':
        return "Won"
    else:
        return False


def validator(x):
    '''
    To check if the position on the board is not overridden
    '''

    # If gameboard ot x has either an X or an O
    # This returns true
    return gb[x] != ' '


def gameplay():
    '''
        Gameplay
    '''


    print(">" * 50 + " TicTacToe " + "<" * 50)
    guide()
    print("\n\n")

    # To choose O or X for player 1
    while True:
        player1 = input("O/X? ").upper()
        if player1 == 'O' or player1 == 'X':
            break
        print("\nChoose again...")

    # Automatically assigns the other value
    if player1 == 'O':
        player2 = 'X'
    else:
        player2 = 'O'

    # loop for the players to take turns to choose positions
    while True:
        print("\n--- PLAYER 1 ---")
        # Enter position and validate
        while True:
            choice1 = input("Enter row and column without space: ")
            if not validator(choice1):
                break
            print("Already occupied, enter again...")

        gb[choice1] = player1 # Update gameboard with X or O
        draw()

        if check() == "Won":
            print("Player 1 Won")
            break
        elif check() == "Game Tied":
            print(check())
            break
        else:
            print()

        print("\n--- PLAYER 2 ---")
        # Enter position and validate
        while True:
            choice2 = input("Enter row and column: ")
            if not validator(choice2):
                break
            print("Already occupied, enter again...")

        gb[choice2] = player2 # Update gameboard with X or O
        draw()

        if check() == "Won":
            print("Player 2 Won")
            break
        elif check() == "Game Tied":
            print(check())
            break
        else:
            print()


# program flow
setgameboard() # compulsory
gameplay()
