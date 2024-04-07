#Q8)Min-Max Algorithm with Alpha Beta Pruning
#This code assumes depth is 3; MAX-MIN-MAX-terminal node

# Initial values of Alpha and Beta
MAX, MIN = 1000, -1000

# Returns optimal value and path for current player
def minimax(node, depth, is_maximizing_player, alpha, beta):
    # Step 3.1: Check if the node is a leaf node
    if depth == 3:
        return node, [node]

    if is_maximizing_player:
        best_val = float('-inf')  # Step 3.2.1
        best_path = []
        for child in range(2):  # Step 3.2.2
            value, path = minimax(node * 2 + child, depth + 1, False, alpha, beta)  # Step 3.2.2.1
            if value > best_val:
                best_val = value
                best_path = [node] + path
            alpha = max(alpha, best_val)  # Step 3.2.2.3
            if beta <= alpha:  # Step 3.2.2.4
                break
        return best_val, best_path

    else:
        best_val = float('inf')  # Step 3.3.1
        best_path = []
        for child in range(2):  # Step 3.3.2
            value, path = minimax(node * 2 + child, depth + 1, True, alpha, beta)  # Step 3.3.2.1
            if value < best_val:
                best_val = value
                best_path = [node] + path
            beta = min(beta, best_val)  # Step 3.3.2.3
            if beta <= alpha:  # Step 3.3.2.4
                break
        return best_val, best_path

# Step 2: Read terminal node values from the user
values = [int(x) for x in input("Enter terminal node values separated by space: ").split()]
# Step 4: Display the optimal value and path
optimal_value, optimal_path = minimax(0, 0, True, MIN, MAX)
print("The optimal value is:", optimal_value)
print("The optimal path is:", optimal_path)
