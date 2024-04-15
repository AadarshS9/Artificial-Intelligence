# Aim
Write a program to implement a tic-tac-toe game in python.

# Theoretical Background
Tic-Tac-Toe is a very popular game for two players, X and O, who take turns marking the space in a 3x3 grid. The player who succeeds in placing 3 of their marks in a horizontal, vertical or diagonal row wins the game. The Tic-Tac-Toe game is based on the minimax algorithm.

# Algorithm
- Step 1: Start.
- Step 2: Create a board using a 2-dimensional array and initialize each element as empty.
- Step 3: Write a function to check whether the board is filled or not. Iterate over the board and return false if the board contains an empty sign or else return true.
- Step 4: Write a function to check whether a player has won or not, i.e., check if 3 same marks are present vertically, horizontally or diagonally.
- Step 5: Write a function to start the game and perform the following operations.
  - Step 5.1: Select the first turn of the player randomly.
  - Step 5.2: Write an infinite loop that breaks when the game is over (either win or draw).
    - Step 5.2.1: Show the board to the user to select the spot for the next move.
    - Step 5.2.2: Ask the user to enter the row and column number.
    - Step 5.2.3: Update the spot with the respective player sign.
    - Step 5.2.4: Check whether the current player won the game or not.
    - Step 5.2.5: If the current player won the game, then print a winning message and break the infinite loop.
    - Step 5.2.6: Check whether the board is filled or not.
    - Step 5.2.7: If the board is filled, then print the draw message and break the infinite loop.
- Step 6: Display the final view of the board.
- Step 7: Stop
