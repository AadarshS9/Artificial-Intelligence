# Aim
Develop a game playing agent for the game Connect Four. The game is played by two players who alternate turns by dropping colored discs into a vertical grid. Each player uses a different color(usually red or yellow), and the objective of the game is to be the first player to get 4 discs in a row.

# Theoretical Background
Connect four is a two player connection game in which the players first choose a color and then take turns dropping colored discs from top into a 7 column, 6 row vertically suspended grid. The pieces fall straight down, occupying the next available space within the column. The objective of the
game is to be the first to form a horizontal, vertical or diagonal line of 4 of one’s own discs.

The connect four uses a minimax algorithm. Everytime the computer decides what move to make next, it considers all its possible moves. The computer then pretends that each of the moves it has considered has actually taken place. For every possible move, it looks at all the moves the other player
could make in response. The algorithm is called minmax because the computer is looking to minimize its maximum losses.

# Algorithm
- Step 1: Start.
- Step 2: Initialize 6x7 matrix with zeros.
- Step 3: Create a stack class or list corresponding to each column to add each array element on top of the previous element in a particular column, in a stacking fashion.
- Step 4: Create a function ‘move()’ and it will have two sections. First section corresponds to the computer&#39;s move, this means that when a certain condition is met, the computer will select an integer between 1 and 7 at random, and a piece will be added to the corresponding stack. The next section corresponds to the human player, here the position to place the next piece is read in the form of an integer, from 1 to 7. It contains four arguments - piece, board, stacks and computer. The arguments ‘board’ and ‘stacks’ are updated during function calls. The arguments ‘piece’ and ‘computer’ correspond to color or pieces.
- Step 5: If piece == computer, it means that it&#39;s the computer’s turn. So the computer chooses a random integer between 1 and 7 and will place a piece in the column corresponding to the chosen number. This happens only if that particular column’s stack is not full, otherwise it will prompt an error. If the stack is full, then the next column is read.
- Step 6: If the piece != computer, it means that it’s human’s turn. A piece is placed corresponding to the column number read from the user after checking if the stack corresponding to the column number is full or not.
- Step 7: Repeat Step 6 until 4 same pieces are in a row or column or in a diagonal.
- Step 8: After placing the pieces, check for the winning conditions, i.e., if the four same pieces are in a row or column or in diagonally. Then the player who has got all four pieces the same in a row or column or diagonal wins.
- Step 9: Stop.
