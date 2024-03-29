#Q6)A* Algorithm
class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Cost from start node to current node
        self.h = h  # Heuristic estimated cost from current node to goal
        self.f = g + h  # Total estimated cost of the cheapest path

def a_star_search(initial_state, goal_state, successors, heuristic):
    open_list = [Node(initial_state, g=0, h=heuristic(initial_state, goal_state))]
    closed_list = []

    while open_list:
        current_node = min(open_list, key=lambda x: x.f)
        open_list.remove(current_node)
        closed_list.append(current_node)

        if current_node.state == goal_state:
            return current_node  # Solution found

        for successor_state, cost in successors(current_node.state):
            successor_node = Node(successor_state, parent=current_node, g=current_node.g + cost,
                                  h=heuristic(successor_state, goal_state))

            if successor_node in closed_list:
                old = [n for n in closed_list if n == successor_node][0]
                if old.g > successor_node.g:
                    old.g = successor_node.g
                    old.parent = successor_node.parent
                    propagate_improvements(old, closed_list)
            elif successor_node in open_list:
                old = [n for n in open_list if n == successor_node][0]
                if old.g > successor_node.g:
                    old.g = successor_node.g
                    old.parent = successor_node.parent
            else:
                open_list.append(successor_node)

    return None  # No solution found

def propagate_improvements(node, closed_list):
    for successor in [n for n in node.parent.successors if n != node]:
        if node.g + node.h < successor.g:
            successor.g = node.g + node.h
            successor.parent = node
            if successor in closed_list:
                propagate_improvements(successor, closed_list)

# Define your heuristic function
def heuristic(state, goal_state):
    # Example: Manhattan distance heuristic for 2D grid
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

# Define your successor function
def successors(state):
    # Example: Generate successors for 2D grid
    x, y = state
    # Example: Movement in 4 directions (up, down, left, right)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    successors = []
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        # Check if the new position is valid (within grid bounds)
        if 0 <= new_x < 10 and 0 <= new_y < 10:  # Adjust the grid dimensions as needed
            successors.append(((new_x, new_y), 1))  # Assuming cost of each movement is 1
    return successors

# Read initial and goal states from the user
initial_state = tuple(map(int, input("Enter initial state (x y): ").split()))
goal_state = tuple(map(int, input("Enter goal state (x y): ").split()))

# Example A* search
result = a_star_search(initial_state, goal_state, successors, heuristic)

# Example: Retrieving the path from start to goal
if result:
    path = []
    current_node = result
    while current_node:
        path.append(current_node.state)
        current_node = current_node.parent
    path.reverse()
    print("Path found:", path)
else:
    print("No path found!")
