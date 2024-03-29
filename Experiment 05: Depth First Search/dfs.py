#Q5)Depth First Search
def dfs(visited, graph, node):
    stack = [node]

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            print(current_node)
            visited.add(current_node)
            for neighbor in graph.get(current_node, []):
              dfs(visited,graph,neighbor)

print("Enter the graph in the form of parent-child pairs.")
print("Enter 'done' when finished.")
graph = {}

while True:
    edge = input("Enter parent-child pair (or 'done' to finish): ").split()
    if edge[0] == 'done' or edge[1] == 'done':
        break
    parent, child = edge
    if parent not in graph:
        graph[parent] = [child]
    else:
        graph[parent].append(child)

print("Graph input completed.\n")
print("Graph:", graph)

visited = set()

print("DFS traversal:")
dfs(visited, graph, next(iter(graph)))
