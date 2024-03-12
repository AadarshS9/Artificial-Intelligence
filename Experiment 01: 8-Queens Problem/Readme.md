# Aim
Write a python program to solve 8 queens problem.

# Theoretical Background
The 8 queens problem is the problem of placing 8 queens on an 8x8 chessboard such that none of them attack one another, i.e., no two are in the same row or column or in adjacent diagonal. More generally, the n queens
problem places n queens on an nxn chessboard. To solve this problem, we make use of the backtracking algorithm. The backtracking algorithm in general checks all possible configurations and tests
whether the required result is obtained or not. For the given problem, we will explore all possible positions the queens can be relatively placed at. The solution will be correct when the number of placed queens is 8.

# Algorithm
- Step 1: Start.
- Step 2: Read the number of queens to be placed from the user and store it in the variable n.
- Step 3: Initialize an nxn matrix.
- Step 4: Create a function ‘placing_queens’ that places the queens on corresponding rows and columns.
- Step 5: Create a function ‘attack’ to check if no queens are placed in the same row or column or in adjacent diagonals.
  - Step 5.1: If two queens are placed on the same row or column, the function should return False.
  - Step 5.2: If two queens are placed in the adjacent diagonal, then the function should return True, else it should return False
- Step 6: Within the function ‘placing_queens’ the following takes place:
  - Step 6.1: As the location of each cell is read, using the function ‘attack’, the cell is checked if it is suitable for placing queens.
  - Step 6.2: If the current row is n, then it means that all the queens are placed at non-attacking positions, so exit from the function ‘palcing_queens’.
  - Step 6.3: Otherwise, traverse through the columns and rows of the current location and check if the function ‘attack’ returns True or False.
    - Step 6.3.1: If there is no queen at the cell read and as well as if the function ‘attack’ returns False, then place queen at that location.
    - Step 6.3.2: Else, read the next location and mark the visited location with 0.
- Step 7: Continue Step 6 until all queens are placed safely at non-attacking positions and display the matrix where the n queens are placed at non-attacking positions.
- Step 8: Stop.

# Solution
- 8queens.py
- 8queens.png
