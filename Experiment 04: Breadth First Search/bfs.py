#Q4)Breadth First Search
print("kindly enter the graph in the form of parent-child pairs.")
print("Kindly enter 'done' when finished.")
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

visited = []
queue = []

def bfs(graph, start_node):
    queue.append(start_node)

    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            print(current_node)
            visited.append(current_node)
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

print("BFS traversal:")
bfs(graph, next(iter(graph)))
