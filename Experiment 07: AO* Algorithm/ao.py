#Q7)AO* Algorithm
def AOStar(n):
    global finalPath
    print("Expanding Node:", n)
    and_nodes = []
    or_nodes = []
    if n in allNodes:
        if 'AND' in allNodes[n]:
            and_nodes = allNodes[n]['AND']
        if 'OR' in allNodes[n]:
            or_nodes = allNodes[n]['OR']
    if len(and_nodes) == 0 and len(or_nodes) == 0:
        return heuristic(n)
    
    solvable = False
    marked = {}
    
    while not solvable:
        if len(marked) == len(and_nodes) + len(or_nodes):
            min_cost_least, min_cost_group_least = least_cost_group(and_nodes, or_nodes, {})
            solvable = True
            change_heuristic(n, min_cost_least)
            optimal_child_group[n] = min_cost_group_least
            continue
        min_cost, min_cost_group = least_cost_group(and_nodes, or_nodes, marked)
        is_expanded = False
        if len(min_cost_group) > 1:
            for node in min_cost_group:
                if node in allNodes:
                    is_expanded = True
                    AOStar(node)
        else:
            if min_cost_group in allNodes:
                is_expanded = True
                AOStar(min_cost_group)
                
        if is_expanded:
            min_cost_verify, min_cost_group_verify = least_cost_group(and_nodes, or_nodes, {})
            if min_cost_group == min_cost_group_verify:
                solvable = True
                change_heuristic(n, min_cost_verify)
                optimal_child_group[n] = min_cost_group
        else:
            solvable = True
            change_heuristic(n, min_cost)
            optimal_child_group[n] = min_cost_group
        marked[min_cost_group] = 1
    return heuristic(n)

def least_cost_group(and_nodes, or_nodes, marked):
    node_wise_cost = {}
    for node_pair in and_nodes:
        if node_pair[0] + node_pair[1] not in marked:
            cost = 0
            cost = cost + heuristic(node_pair[0]) + heuristic(node_pair[1]) + 2
            node_wise_cost[node_pair[0] + node_pair[1]] = cost
    for node in or_nodes:
        if node not in marked:
            cost = 0
            cost = cost + heuristic(node) + 1
            node_wise_cost[node] = cost
    min_cost = 999999
    min_cost_group = None
    for costKey in node_wise_cost:
        if node_wise_cost[costKey] < min_cost:
            min_cost = node_wise_cost[costKey]
            min_cost_group = costKey
    return min_cost, min_cost_group

def heuristic(n):
    return H_dist[n]

def change_heuristic(n, cost):
    H_dist[n] = cost

def print_path(node):
    print(optimal_child_group[node], end="")
    node = optimal_child_group[node]
    if len(node) > 1:
        if node[0] in optimal_child_group:
            print(" -> ", end="")
            print_path(node[0])
        if node[1] in optimal_child_group:
            print(" -> ", end="")
            print_path(node[1])
    else:
        if node in optimal_child_group:
            print(" -> ", end="")
            print_path(node)
            
H_dist = {'A': -1, 'B': 4, 'C': 2, 'D': 3, 'E': 6, 'F': 8, 'G': 2, 'H': 0, 'I': 0, 'J': 0}

allNodes = {
    'A': {'AND': [('C', 'D')], 'OR': ['B']},
    'B': {'OR': ['E', 'F']},
    'C': {'OR': ['G'], 'AND': [('H', 'I')]},
    'D': {'OR': ['J']}
}

startnode = 'A'
goalnode = 'J'
print("\n")

optimal_child_group = {}
optimal_cost = AOStar(startnode)

if goalnode not in optimal_child_group.values():
    print("\nPath from", startnode, "to", goalnode, "not present")
else:
    print("\nNodes which give optimal cost from the start node", startnode, "are:")
    print_path(startnode)
    print('\n\nOptimal cost is', optimal_cost)
