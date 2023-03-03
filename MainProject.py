from random import choice

def InitializeGrid(board): # Initialize grid using an array
    
    for i in range(8):
        for j in range(8):
            board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])


def Initialize(board):
    
    InitializeGrid(board)
    global score
    score = 0
    global turn
    turn = 1


def ContinueGame(current_score, goal_score = 100):
    
    if (current_score >= goal_score):
        return False
    else:
        return True

def DrawBoard(board):
    
    print("\nMatch 3 Letters Either Horizontally or Vertically within the Grid\n\n")
    print("   ---------------------------------")
    # Draw 8 rows unto the terminal, starting from the last row
    for i in range(7, -1, -1):                                                                                                                                               
        #Individual rows
        linetodraw = ""
        for j in range(8):
            linetodraw += " | " + board[i][j]
        linetodraw += " |"
        print(f"{i+1} {linetodraw}")
        print("   ---------------------------------")
    print("     a   b   c   d   e   f   g   h")
    global score
    print(f"Current Score: {score}\n")

def IsValid(move):
    
    if len(move) != 3:
        return False

    # Validates space and direction of move
    if not move[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        return False
    if not move[1] in ['1', '2', '3', '4', '5', '6', '7', '8']:
        return False
    if not move[2] in ['u', 'd', 'l', 'r']:
        return False

    #Check that first column moves are not left
    if move[0] == 'a' and move[2] == 'l':
        return False
    # Check that last column moves are not right
    if move[0] == 'h' and move[2] == 'r':
        return False
    # Check that bottom row moves are not down
    if move[1] == '1' and move[2] == 'd':
        return False
    # Check that top row moves are not up
    if move[1] == '8' and move[2] == 'u':
        return False

    return True

def GetMove():
    
    print("""Play by choosing the Letter(intersection of a column and row) to swap and the direction (u,d,l,r).
    Input should list column first then row.
    Columns are alphabetical from a - h
    Rows are counted from the bottom starting from 1.
    
    Example, "e3u" will swap position e3 with the one above, 
    and "f7r" will swap f7 to the right.
    
    Enter exit to quit""")
    
    move = input("Enter move: ")
    
    if move == "exit":
        exit()

    while not IsValid(move):
        move = input("Invalid direction specified! Enter another move:")
        
    return move

def ConvertLetterToCol(Col):
    
    if Col == 'a':
        return 0
    elif Col == 'b':
        return 1
    elif Col == 'c':
        return 2
    elif Col == 'd':
        return 3
    elif Col == 'e':
        return 4
    elif Col == 'f':
        return 5
    elif Col == 'g':
        return 6
    elif Col == 'h':
        return 7
    else:
        #Invalid column
        return -1

def SwapPieces(board, move):
    
    # Get selected position
    sel_row = int(move[1]) - 1
    sel_col = ConvertLetterToCol(move[0])
    
    # Get adjacent position
    if move[2] == 'u':
        new_row = sel_row + 1
        new_col = sel_col
    elif move[2] == 'd':
        new_row = sel_row - 1
        new_col = sel_col
    elif move[2] == 'l':
        new_row = sel_row
        new_col = sel_col - 1
    elif move[2] == 'r':
        new_row = sel_row
        new_col = sel_col + 1
        
    # Swap selected character
    temp = board[sel_row][sel_col]
    board[sel_row][sel_col] = board[new_row][new_col]
    board[new_row][new_col] = temp

def RemoveAndScorePieces(board): # Score and remove 3 matching pieces
    
    # Create a new board to remove and score matching characters
    remove = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    
    # Go through rows
    for i in range(8):
        for j in range(6):
            if (board[i][j] == board[i][j + 1]) and (board[i][j] == board[i][j + 2]):
                # three in a row are matching
                remove[i][j] = 1;
                remove[i][j + 1] = 1;
                remove[i][j + 2] = 1;

    # Go through columns
    for j in range(8):
        for i in range(6):
            if (board[i][j] == board[i + 1][j]) and (board[i][j] == board[i + 2][j]):
                # three in a row are matching
                remove[i][j] = 1;
                remove[i + 1][j] = 1;
                remove[i + 2][j] = 1;

    # Eliminate letters marked within remove board from main board
    global score
    removed_any = False
    for i in range(8):
        for j in range(8):
            if remove[i][j] == 1:
                board[i][j] = 0
                score += 1
                removed_any = True
                
    return removed_any

def DropPieces(board): # Drop remaining letter pieces down to fill in blanks
    
    for j in range(8):
        # var to store remaining letters
        listofpieces = []
        
        for i in range(8):
            # get column letter if not removed
            if board[i][j] != 0:
                listofpieces.append(board[i][j])
        # insert remaining letters into the column
        for i in range(len(listofpieces)):
            board[i][j] = listofpieces[i]
        # fill in remainder of column with 0s
        for i in range(len(listofpieces), 8):
            board[i][j] = 0

def FillBlanks(board):
    
    for i in range(8):
        for j in range(8):
            if (board[i][j] == 0):
                board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])

def Update(board, move): # Update board values
    
    SwapPieces(board, move)
    
    while RemoveAndScorePieces(board):
        DropPieces(board)
        FillBlanks(board)

def DoRound(board):
    
    DrawBoard(board)
    move = GetMove()
    Update(board, move)
    global turn
    turn += 1



#Global variables
score = 0
turn = 0
goalscore = 100
board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

#Initialize game
print("Game ends when specified score is achieved.\nCorrect moves net an average of 16 points due to cascades.\n")
while True:
    try:
        score = int(input("Input your desired score to end game at.\n->"))
        break
    except:
        print("Invalid number provided")

Initialize(board)

#While game not over
while ContinueGame(score, goalscore):
    #Do a round of the game)
    DoRound(board)
print(f"\n->A winner is you with {score}points!")