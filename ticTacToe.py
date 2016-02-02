
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################

    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################

    return ((board[7]==player and board[8]==player and board[9]==player) or
    (board[4]==player and board[5]==player and board[6]==player) or
    (board[1]==player and board[2]==player and board[3]==player) or
    (board[7]==player and board[4]==player and board[1]==player) or
    (board[8]==player and board[5]==player and board[2]==player) or
    (board[9]==player and board[6]==player and board[3]==player) or
    (board[7]==player and board[5]==player and board[3]==player) or
    (board[9]==player and board[5]==player and board[1]==player))

    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer
    for i in range(9):
        printBoard(board) #The new code prints out the board at the start of each new turn.
        print('Turn for ' + turn + '. Move on which space?')
        move = input() #gets the active players move
        board[move] = turn #updates the game board accordingly
        if( checkWinner(board, 'X') ): #swaps the active player before moving on to the next turn
            print('X wins!')
            break
        elif ( checkWinner(board, 'O') ):
            print('O wins!')
            break
    
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
    printBoard(board)
    
