# TICTACTOE
#### Video Demo:  <https://youtu.be/BuiVwU55l6s>
#### Description: This is a tictactoe game made using python
It uses min-max algorithm (https://en.wikipedia.org/wiki/Minimax)

pygame library was used in this project : It is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.
'
#### IMPORTANT NOTE:  run "pip3 install -r requirements.txt" to install the required Python package (pygame) for this project. After this Run "python runner.py" to play against the AI

How minimax algorithm works:
A type of algorithm in adversarial search, Minimax represents winning conditions as (-1) for one side and (+1) for the other side. Further actions will be driven by these conditions, with the minimizing side trying to get the lowest score, and the maximizer trying to get the highest score.

Recursively, the algorithm simulates all possible games that can take place beginning at the current state and until a terminal state is reached. Each terminal state is valued as either (-1), 0, or (+1).

Knowing based on the state whose turn it is, the algorithm can know whether the current player, when playing optimally, will pick the action that leads to a state with a lower or a higher value. This way, alternating between minimizing and maximizing, the algorithm creates values for the state that would result from each possible action. To give a more concrete example, we can imagine that the maximizing player asks at every turn: “if I take this action, a new state will result. If the minimizing player plays optimally, what action can that player take to bring to the lowest value?” However, to answer this question, the maximizing player has to ask: “To know what the minimizing player will do, I need to simulate the same process in the minimizer’s mind: the minimizing player will try to ask: ‘if I take this action, what action can the maximizing player take to bring to the highest value?’” This is a recursive process, and it could be hard to wrap your head around it; looking at the pseudo code below can help. Eventually, through this recursive reasoning process, the maximizing player generates values for each state that could result from all the possible actions at the current state. After having these values, the maximizing player chooses the highest one.

The Maximizer Considers the Possible Values of Future States.

To put it in pseudocode, the Minimax algorithm works the following way:

Given a state s
    The maximizing player picks action a in Actions(s) that produces the highest value of Min-Value(Result(s, a)).
    The minimizing player picks action a in Actions(s) that produces the lowest value of Max-Value(Result(s, a)).


Function Max-Value(state)
    v = -∞
    
    if Terminal(state):
    return Utility(state)
    
    for action in Actions(state):
    v = Max(v, Min-Value(Result(state, action)))
    return v

Function Min-Value(state):
    v = ∞
    
    if Terminal(state):
    return Utility(state)

    for action in Actions(state):
    v = Min(v, Max-Value(Result(state, action)))
    
    return v


runner.py basically handles the visual representation or game part of it using pygame.

tictactoe.py handles the logic behind the AI
Inside this, 
player function - takes a board state as input, and return which player’s turn it is (either X or O).
actions function -returns a set of all of the possible actions that can be taken on a given board.
result function -takes a board and an action as input, and returns a new board state, without modifying the original board.
winner function - accepts a board as input, and returns the winner of the board if there is one.
terminal function - accepts a board as input, and returns a boolean value indicating whether the game is over.
utility function - accepts a terminal board as input and outputs the utility of the board.
minimax function - takes a board as input, and returns the optimal move for the player to move on that board.

To run:
First run "pip3 install -r requirements.txt" in the terminal to downlaod the library pygame

You should have python installed to run it 
Type "python runner.py" to run this project. 

As the AI is very strong in this, humans cant win generally.
THe only possible outcomes are tie, draw.

You can play aS X or O. The computer will play the other one.

Alternatively Alpha- beta pruning could also be used for this project but i Found that tricky.

