#!/usr/bin/env python3
"""
tahera_MS24xx_GA.py
Traveling Salesman Problem solved by a Genetic Algorithm.

- Reads cities from 'India_cities_GA.txt' (format: CityName x y per line)
- Shows intermediate path tracing with city names
- Plots average fitness (and best fitness) vs generations at the end
- Saves intermediate path images (path_gen_0.png, path_gen_50.png, ...)

Usage:
    python tahera_MS24xx_GA.py
"""

import random
import math
import matplotlib.pyplot as plt
import os
from typing import List, Tuple

# -------------------------
# Configuration / GA params
# -------------------------
DATA_FILE = "India_cities_GA.txt"
POPULATION_SIZE = 200
GENERATIONS = 500
TOURNAMENT_SIZE = 5
ELITISM = 2
CROSSOVER_RATE = 0.9
MUTATION_RATE = 0.2
PLOT_INTERVAL = 50  # show/save the best path every PLOT_INTERVAL generations
SAVE_PLOTS_DIR = "ga_path_plots"
RANDOM_SEED = 42

random.seed(RANDOM_SEED)

# -------------------------
# Utility / Data structures
# -------------------------
def read_cities(filename: str) -> List[Tuple[str, float, float]]:
    """Read city_name, x, y from file."""
    cities = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) < 3:
                continue
            name = parts[0]
            try:
                x = float(parts[-2])
                y = float(parts[-1])
            except ValueError:
                # try comma separated coords like "name x,y"
                coords = parts[1].split(",")
                x = float(coords[0])
                y = float(coords[1])
            cities.append((name, x, y))
    return cities

def euclidean(a: Tuple[float,float], b: Tuple[float,float]) -> float:
    return math.hypot(a[0]-b[0], a[1]-b[1])

def total_distance(tour: List[int], coords: List[Tuple[float,float]]) -> float:
    dist = 0.0
    for i in range(len(tour)):
        a = coords[tour[i]]
        b = coords[tour[(i+1) % len(tour)]]
        dist += euclidean(a, b)
    return dist

# -------------------------
# GA operators
# -------------------------
def create_random_tour(n_cities: int) -> List[int]:
    tour = list(range(n_cities))
    random.shuffle(tour)
    return tour

def initial_population(size: int, n_cities: int) -> List[List[int]]:
    return [create_random_tour(n_cities) for _ in range(size)]

def fitness_of(tour: List[int], coords: List[Tuple[float,float]]) -> float:
    # higher fitness = better. We want to minimize distance, so use inverse.
    dist = total_distance(tour, coords)
    # avoid division by zero
    return 1.0 / (dist + 1e-9)

def tournament_selection(population: List[List[int]], fitnesses: List[float], k: int) -> List[int]:
    selected_idx = random.sample(range(len(population)), k)
    best = max(selected_idx, key=lambda i: fitnesses[i])
    return population[best][:]  # return a copy

def ordered_crossover(parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
    # OX crossover
    n = len(parent1)
    a, b = sorted(random.sample(range(n), 2))
    def ox(p1, p2):
        child = [-1]*n
        # copy slice from p1
        child[a:b+1] = p1[a:b+1]
        # fill remaining from p2 in order
        cur = 0
        for gene in p2:
            if gene in child:
                continue
            while child[cur] != -1:
                cur += 1
            child[cur] = gene
        return child
    return ox(parent1, parent2), ox(parent2, parent1)

def swap_mutation(tour: List[int], mutation_rate: float) -> None:
    n = len(tour)
    for i in range(n):
        if random.random() < mutation_rate:
            j = random.randrange(n)
            tour[i], tour[j] = tour[j], tour[i]

# -------------------------
# Visualization helpers
# -------------------------
def plot_tour(coords: List[Tuple[float,float]], names: List[str], tour: List[int],
              title: str = "", show: bool = True, savepath: str = None):
    """Plot the given tour with city names annotated and lines connecting them."""
    xs = [coords[i][0] for i in tour] + [coords[tour[0]][0]]
    ys = [coords[i][1] for i in tour] + [coords[tour[0]][1]]
    plt.figure(figsize=(10, 8))
    plt.plot(xs, ys, linestyle='-', marker='o')
    for idx, city_idx in enumerate(tour):
        x, y = coords[city_idx]
        plt.annotate(f"{names[city_idx]} ({idx})", (x, y), textcoords="offset points", xytext=(3,3), fontsize=8)
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    if savepath:
        plt.savefig(savepath, bbox_inches='tight')
    if show:
        plt.show()
    plt.close()

# -------------------------
# Genetic Algorithm run
# -------------------------
def run_ga(cities, pop_size=POPULATION_SIZE, generations=GENERATIONS):
    names = [c[0] for c in cities]
    coords = [(c[1], c[2]) for c in cities]
    n = len(cities)
    if n < 2:
        raise ValueError("Need at least 2 cities for TSP.")
    if not os.path.exists(SAVE_PLOTS_DIR):
        os.makedirs(SAVE_PLOTS_DIR)

    # initialize population
    population = initial_population(pop_size, n)
    fitnesses = [fitness_of(t, coords) for t in population]

    avg_fitness_history = []
    best_fitness_history = []
    best_tour = None
    best_distance = float("inf")

    # plot initial best
    cur_best_idx = max(range(len(population)), key=lambda i: fitnesses[i])
    cur_best = population[cur_best_idx]
    cur_best_dist = total_distance(cur_best, coords)
    best_tour, best_distance = cur_best[:], cur_best_dist

    print(f"Initial best distance: {best_distance:.4f}")
    plot_tour(coords, names, best_tour, title=f"Generation 0 — best dist {best_distance:.2f}",
              show=True, savepath=os.path.join(SAVE_PLOTS_DIR, "path_gen_0.png"))

    for gen in range(1, generations+1):
        new_pop = []

        # elitism: keep top ELITISM individuals
        sorted_idx = sorted(range(len(population)), key=lambda i: fitnesses[i], reverse=True)
        for e in range(ELITISM):
            new_pop.append(population[sorted_idx[e]][:])

        # generate new individuals
        while len(new_pop) < pop_size:
            parent1 = tournament_selection(population, fitnesses, TOURNAMENT_SIZE)
            parent2 = tournament_selection(population, fitnesses, TOURNAMENT_SIZE)
            if random.random() < CROSSOVER_RATE:
                child1, child2 = ordered_crossover(parent1, parent2)
            else:
                child1, child2 = parent1[:], parent2[:]

            # mutation
            swap_mutation(child1, MUTATION_RATE)
            swap_mutation(child2, MUTATION_RATE)

            new_pop.append(child1)
            if len(new_pop) < pop_size:
                new_pop.append(child2)

        population = new_pop
        fitnesses = [fitness_of(t, coords) for t in population]

        avg_fit = sum(fitnesses) / len(fitnesses)
        best_idx = max(range(len(population)), key=lambda i: fitnesses[i])
        best_t = population[best_idx]
        best_d = total_distance(best_t, coords)

        avg_fitness_history.append(avg_fit)
        best_fitness_history.append(fitnesses[best_idx])

        if best_d < best_distance:
            best_distance = best_d
            best_tour = best_t[:]

        # print progress at intervals
        if gen % (PLOT_INTERVAL // 2 or 1) == 0:
            print(f"Gen {gen:4d}: avg fitness={avg_fit:.6e}, best dist={best_d:.4f}")

        # save/plot intermediate best tours every PLOT_INTERVAL generations
        if gen % PLOT_INTERVAL == 0 or gen == generations:
            title = f"Generation {gen} — best dist {best_d:.2f}"
            savepath = os.path.join(SAVE_PLOTS_DIR, f"path_gen_{gen}.png")
