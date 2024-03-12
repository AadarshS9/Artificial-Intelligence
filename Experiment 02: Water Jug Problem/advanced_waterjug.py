from collections import deque

def WaterJugSolver(jug1, jug2, aim):
    visited = set()
    queue = deque([(0, 0)])
    path = {}

    while queue:
        current_state = queue.popleft()
        if current_state == aim:
            break

        for next_state in next_states(jug1, jug2, current_state):
            if next_state not in visited:
                queue.append(next_state)
                visited.add(next_state)
                path[next_state] = current_state

    # Reconstruct path
    solution = [aim]
    while aim != (0, 0):
        aim = path[aim]
        solution.append(aim)
    solution.reverse()
    return solution

def next_states(jug1, jug2, state):
    x, y = state
    next_states = set()

    # Rule 1: Fill the m gallon jug completely
    next_states.add((jug1, y))
    # Rule 2: Fill the n gallon jug completely
    next_states.add((x, jug2))
    # Rule 3: Pour some part of m gallon jug
    next_states.add((0, y))
    # Rule 4: Pour some part of n gallon jug
    next_states.add((x, 0))
    # Rule 5: Empty m gallon jug
    next_states.add((0, y))
    # Rule 6: Empty n gallon jug
    next_states.add((x, 0))
    # Rule 7: Pour some water from the n gallon jug to fill the m gallon jug
    next_states.add((min(x + y, jug1), max(0, x + y - jug1)))
    # Rule 8: Pour some water from the m gallon jug to fill the n gallon jug
    next_states.add((max(0, x + y - jug2), min(x + y, jug2)))

    return next_states

def print_solution(solution):
    print("Path to reach the aim:")
    for state in solution:
        print(state)

# Main Program
print("Water Jug Problem Solver")
print("Enter capacities of jug 1 and jug 2:")
jug1 = int(input("Jug 1 Capacity: "))
jug2 = int(input("Jug 2 Capacity: "))
aim_x = int(input("Enter the amount of water to be present in jug 1: "))
aim_y = int(input("Enter the amount of water to be present in jug 2: "))
aim = (aim_x, aim_y)

solution = WaterJugSolver(jug1, jug2, aim)
print_solution(solution)
