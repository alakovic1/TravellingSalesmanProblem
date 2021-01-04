import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
import numpy as np
import matplotlib.pyplot as plt
import math as m

def NacrtajGraf(naziv, x, y):
    plt.grid(True)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    #TACKE
    plt.plot(x, y, color='red', marker='o')
    plt.title(naziv)

# Create list of city coordinates
coords_list = [(1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6), (1, 5), (2, 3), (6, 3), (2, 2), (2, 1)]

# Initialize fitness function object using coords_list
fitness_coords = mlrose.TravellingSales(coords = coords_list)

problem_fit = mlrose.TSPOpt(length = len(coords_list), fitness_fn = fitness_coords, maximize=False)

# Solve problem using the genetic algorithm
#best_state, best_fitness = mlrose.genetic_alg(problem_fit, random_state = 2)
best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2, max_attempts = 100, random_state = 2)

print('The best state found is: ', best_state)

print('The fitness at the best state is: ', best_fitness)

plt.figure()
for cl in coords_list:
    NacrtajGraf('$Travelling Salesman Problem$', cl[0], cl[1])
plt.show()


