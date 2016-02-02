#Lam Le
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

    return ((board['top-L']==player and board['top-M']==player and board['top-R']==player) or #across the top 
    (board['mid-L']==player and board['mid-M']==player and board['mid-R']==player) or #across the middle
    (board['low-L']==player and board['low-M']==player and board['low-R']==player) or #across the bottom
    (board['top-L']==player and board['mid-L']==player and board['low-L']==player) or #down the left side
    (board['top-M']==player and board['mid-M']==player and board['low-M']==player) or #down the middle
    (board['top-R']==player and board['mid-R']==player and board['low-R']==player) or #down the right side
    (board['top-L']==player and board['mid-M']==player and board['low-R']==player) or #diagonal
    (board['top-R']==player and board['mid-M']==player and board['low-L']==player)) #diagonal

    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer #1st players move
    for i in range(9): #loops through the 9 squares
        printBoard(board) #The new code prints out the board at the start of each new turn.
        print('Turn for ' + turn + '. Move on which space?') #prints the persons turn
        move = input() #gets the active players move
        board[move] = turn #updates the game board accordingly
        if( checkWinner(board, 'X') ): #swaps the active player before moving on to the next turn
            print('X wins!') #prints X wins
            break #Exit
        elif ( checkWinner(board, 'O') ): #Checks to see no one wins
            print('O wins!') #states that O WINS
            break #Exits
    
        if turn == 'X': #player X turn 
            turn = 'O' #player 0 turn
        else:
            turn = 'X' #player X turn
        
    printBoard(board) 
    
