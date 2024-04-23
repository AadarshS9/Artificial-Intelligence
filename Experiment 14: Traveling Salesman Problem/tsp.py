# Q14) Traveling Salesman Problem
import random
import math

# Step 2: Define the cities, distances between them, and starting city
cities = ['A', 'B', 'C', 'D']
distances = [
    [math.inf, 10, 15, 20],
    [10, math.inf, 35, 25],
    [15, 35, math.inf, 30],
    [20, 25, 30, math.inf],
]
start_city = 'A'

def generate_initial_solution():
    # Step 3: Create an initial solution
    route = [start_city]
    unvisited_cities = cities.copy()
    unvisited_cities.remove(start_city)
    
    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: distances[cities.index(route[-1])][cities.index(city)])
        route.append(nearest_city)
        unvisited_cities.remove(nearest_city)
    
    return route

def total_distance(route):
    # Step 4: Calculate the total distance of the route
    total = 0
    for i in range(len(route) - 1):
        total += distances[cities.index(route[i])][cities.index(route[i + 1])]
    total += distances[cities.index(route[-1])][cities.index(route[0])]  # Return to starting city
    return total

def improve_solution(route):
    # Step 5: Improve the solution by swapping cities
    improved = False
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            new_route = route[:]
            new_route[i], new_route[j] = new_route[j], new_route[i]  # Swap cities
            new_distance = total_distance(new_route)
            if new_distance < total_distance(route):
                route = new_route
                improved = True
    return route, improved

def tsp():
    # Step 1: Start
    best_route = None
    best_distance = float('inf')
    
    # Step 6: Repeat until satisfactory solution is found or a stopping criterion is met
    while True:
        # Step 3: Create an initial solution
        current_route = generate_initial_solution()
        
        # Step 4: Calculate the total distance of the route
        current_distance = total_distance(current_route)
        
        # Step 5: Improve the solution
        current_route, improved = improve_solution(current_route)
        
        # Check if the improved solution is better than the best solution found so far
        if current_distance < best_distance:
            best_route = current_route
            best_distance = current_distance
        
        # Step 6: Repeat steps 4 and 5 until stopping criterion is met
        if not improved:
            break
    
    # Step 7: Return the best solution
    return best_route

# Step 8: Stop

# Solve the TSP
best_route = tsp()
best_distance = total_distance(best_route)
best_route.append(start_city)  # Append the starting city to complete the cycle
print("Best Route:", best_route)
print("Total Distance:", best_distance)
