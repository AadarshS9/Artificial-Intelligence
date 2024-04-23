# Q14) Traveling Salesman Problem
from sys import maxsize
from itertools import permutations

def travellingSalesmanProblem(cities, graph, start_city):
    n = len(graph)
    vertex = [i for i in range(n) if i != start_city]

    min_path = maxsize
    min_path_order = None
    next_permutation = permutations(vertex)
    
    for perm in next_permutation:
        current_path_weight = 0
        k = start_city
        path_order = [cities[start_city]]
        
        for j in perm:
            current_path_weight += graph[k][j]
            k = j
            path_order.append(cities[j])
            
        current_path_weight += graph[k][start_city]
        path_order.append(cities[start_city])
        
        if current_path_weight < min_path:
            min_path = current_path_weight
            min_path_order = path_order

    return min_path, min_path_order


cities = ['A', 'B', 'C', 'D']
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
start_city = 0
min_path_length, min_path_order = travellingSalesmanProblem(cities, graph, start_city)
print("Shortest path length:", min_path_length)
print("Shortest path order:", min_path_order)
