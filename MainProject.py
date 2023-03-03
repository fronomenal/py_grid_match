from random import choice

def InitializeGrid(board): # Initialize grid using an array
    pass


def Initialize(board):
   pass


def ContinueGame(current_score, goal_score = 100):
    pass

def DrawBoard(board):
    pass

def IsValid(move):
    pass

def GetMove():
    pass

def ConvertLetterToCol(Col):
    pass

def SwapPieces(board, move):
    pass

def RemovePieces(board): # Remove 3 matching pieces
    pass

def DropPieces(board): # Drop pieces to fill in blanks
    pass

def FillBlanks(board):
    pass

def Update(board, move):
    pass

def DoRound(board):
    pass



#Global variables
score = 0
turn = 0
goalscore = 100
board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

#Initialize game
Initialize(board)

#While game not over
while ContinueGame(score, goalscore):
    #Do a round of the game)
    DoRound(board)