##  GENETIC ALGORITHM 
# Population = random paths (tours).

# Fitness = total distance (lower is better).

# Selection = choose good parents (tournament selection).

# Crossover = combine two parents to make a child (order crossover).

# Mutation = swap cities randomly to introduce variety.

# Repeat for many generations until convergence.

# -- Individuals are represented by "Chromosomes"
# in tsp all routes treat as individual such [ Karachi, lahore, islamabad ] 

import random
import numpy as np

# --- Distance Function ---
def distance(path, dist_matrix):
    """Calculate total distance of a path based on dist_matrix"""
    return sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1)) + dist_matrix[path[-1]][path[0]]

# --- Create Initial Population ---
def create_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        path = list(range(num_cities))
        random.shuffle(path)
        population.append(path)
    return population

# --- Selection (Tournament) ---
def selection(population, dist_matrix, k=3):
    selected = random.sample(population, k)
    selected.sort(key=lambda path: distance(path, dist_matrix))
    return selected[0]

# --- Crossover (Order Crossover) ---
def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = parent1[start:end]

    fill_positions = [i for i in range(size) if child[i] is None]
    parent2_nodes = [node for node in parent2 if node not in child]

    for pos, node in zip(fill_positions, parent2_nodes):
        child[pos] = node

    return child

# --- Mutation (Swap) ---
def mutate(path, mutation_rate=0.1):
    path = path[:]
    for i in range(len(path)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(path)-1)
            path[i], path[j] = path[j], path[i]
    return path

# --- Genetic Algorithm ---
def genetic_algorithm_tsp(dist_matrix, pop_size=100, generations=500, mutation_rate=0.1):
    num_cities = len(dist_matrix)
    population = create_population(pop_size, num_cities)

    best_path = min(population, key=lambda path: distance(path, dist_matrix))
    best_distance = distance(best_path, dist_matrix)

    for gen in range(generations):
        new_population = []
        for _ in range(pop_size):
            parent1 = selection(population, dist_matrix)
            parent2 = selection(population, dist_matrix)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population
        current_best = min(population, key=lambda path: distance(path, dist_matrix))
        current_distance = distance(current_best, dist_matrix)

        if current_distance < best_distance:
            best_path, best_distance = current_best, current_distance

        if gen % 50 == 0:
            print(f"Gen {gen}: Best Distance = {best_distance}")

    return best_path, best_distance


# --- Example Usage ---
dist_matrix = [
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]
]

best_path, best_dist = genetic_algorithm_tsp(dist_matrix, pop_size=50, generations=300, mutation_rate=0.05)
print("\nBest Path:", best_path)
print("Best Distance:", best_dist)
