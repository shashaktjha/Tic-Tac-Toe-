"""
Tic Tac Toe Player
"""
from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    # Loop for getting the number of X's and O's in the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == X:
                x += 1
            elif board[i][j] == O:
                o += 1

    # if number of X's = O's then its X's turn and if X > O then O's turn
    if x > o:
        return O
    elif x == o:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    a = set()
    # Whichever spot is empty is appended to set a
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                a.add((i,j))
    return a


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Checking for valid action
    for i in action:
        if i not in [0,1,2]:
            raise Exception("Invalid Action")
    """
     Creating deepcopy of original board and changing the value
     at index specified by action for player returned by player function
    """
    li = deepcopy(board)
    li[action[0]][action[1]] = player(board)
    
    return li


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        # if all 3 elements in a row are same
        if all(v == board[i][0] for v in board[i]) and board[i][0] != EMPTY:
            return board[i][0]
        # if all 3 elements in a column are same
        if board[0][i] == board [1][i] == board[2][i] != EMPTY:
            return board[0][i]    

    # checking for Diagonal elements 
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY :  
        return board[1][1]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Checking if theres a winner
    if winner(board) != None:
        return True
    # if theres an empty tile that means game isnt over
    for i in board:
        for j in i:
            if j == EMPTY:
                return False    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 1 if winner(board) == X else  -1 if winner(board) == O else  0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Checking if the game is over
    if terminal(board):
        return None
    # Calling Minvalue of next layer if AI wants to Play as X
    if player(board) == X:
        v = -2
        # Choosing the Highest Value Out of the First Layer 
        for action in actions(board):
            # calling Minvalue for next layer as next layer would be chosen by player O
            if MinValue(result(board, action)) > v:
                v = MinValue(result(board,action))
                act = action
    else:
        v = 2 
        # Choosing the lowest Value Out of the First Layer 
        for action in actions(board):
            # calling Maxvalue for next layer as next layer would be chosen by player X
            if MaxValue(result(board,action)) < v:
                v = MaxValue(result(board,action))
                act = action
    return act

def MaxValue(board):
    # Recursively calling to get the value
    v = -2
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, MinValue(result(board, action)))
    return v


def MinValue(board):
    # Recursively calling to get the value
    v = 2
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, MaxValue(result(board, action)))
    return v