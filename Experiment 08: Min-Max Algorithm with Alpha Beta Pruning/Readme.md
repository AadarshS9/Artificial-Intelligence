# Aim:
Write a program to implement the Min-Max algorithm with alpha beta pruning.

# Theoretical Background:
The minimax algorithm is a relatively simple algorithm used for optimal decision making in game theory and artificial intelligence. Alpha-beta pruning is an optimization technique for the minimax algorithm. It reduces the
computation time by a huge factor. This allows us to search much faster and even go into deeper levels in the game tree. It cuts off branches in the game tree which need not be searched because there already exists a better move
available. It is called alpha-beta pruning because it passes two extra parameters in the minimax function, namely alpha and beta. Alpha is the best value that the minimizer currently can guarantee at that level or above. Beta is the best value that the minimizer currently can
guarantee at that level or below. 

# Algorithm:
- Step 1: Start.
- Step 2: Read the terminal node values from the user and pass it to the function to perform min-max with alpha beta pruning.
- Step 3: Create the function ‘minmax’ with parameters node, depth, isMaximizingPlayer, alpha and beta to perform minimax pruning. Perform the following within the function ‘minimax’.
  - Step 3.1: Check if the node is a leaf node, then return the value of the node.
  - Step 3.2: Check if the ‘isMaximizingPlayer’ is true, then do the following.
    - Step 3.2.1: Initialize bestVal = -infinity.
    - Step 3.2.2: For each child node, perform the following.
      - Step 3.2.2.1: Call the function ‘minimax’ and pass the argument node, depth+1, false, alpha and beta. Store the return value from this function call to the variable ‘value’.
      - Step 3.2.2.2: Choose the maximum of bestVal and value and store it in bestVal.
      - Step 3.2.2.3: Choose the maximum value of alpha and bestVal and store it in alpha.
      - Step 3.2.2.4: Check if beta&lt;=alpha, then break and return the value of bestVal to the calling variable.
  - Step 3.3: Otherwise, perform the following.
    - Step 3.3.1: Initialize bestVal = +infinity.
    - Step 3.3.2: For each child node, perform the following.
      - Step 3.3.2.1: Call the function ‘minimax’ and pass the argument node, depth+1, true, alpha and beta. Store the return value from this function call to the variable ‘value’.
      - Step 3.3.2.2: Choose the minimum of bestVal and value and store it in bestVal.
      - Step 3.3.2.3: Choose the minimum value of beta and bestVal and store it in beta.
      - Step 3.3.2.4: Check if beta&lt;=alpha, then break and return the value of bestVal to the calling variable.
- Step 4: Display the best value from the minimax function as the optimal value.
- Step 5: Stop.
