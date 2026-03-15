import numpy as np
import matplotlib.pyplot as plt
import random

# Parametry
size = 10  # Dla testów - potem 200
empty_ratio = 0.1
tolerance = 0.20
max_iters = 500

# Reprezentacja agentów
EMPTY = 0
RED = 1
GREEN = 2

def create_grid(size, empty_ratio):
    total_cells = size * size
    num_empty = int(total_cells * empty_ratio)
    num_agents = total_cells - num_empty

    agents = [RED] * (num_agents // 2) + [GREEN] * (num_agents // 2) + [EMPTY] * num_empty
    random.shuffle(agents)
    return np.array(agents).reshape((size, size))

def get_neighbors(grid, x, y):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]:
                neighbors.append(grid[nx][ny])
    return neighbors

def is_unsatisfied(grid, x, y, tolerance):
    agent = grid[x][y]
    if agent == EMPTY:
        return False

    neighbors = get_neighbors(grid, x, y)
    if not neighbors:
        return False

    different = sum(1 for n in neighbors if n != agent and n != EMPTY)
    total = sum(1 for n in neighbors if n != EMPTY)
    if total == 0:
        return False

    return (different / total) > tolerance

def relocate(grid, x, y, empty_cells):
    if not empty_cells:
        return
    new_x, new_y = random.choice(empty_cells)
    grid[new_x][new_y] = grid[x][y]
    grid[x][y] = EMPTY
    empty_cells.remove((new_x, new_y))
    empty_cells.append((x, y))

def simulate(grid, tolerance, max_iters):
    for it in range(max_iters):
        unsatisfied = []
        empty_cells = [(x, y) for x in range(grid.shape[0])
                              for y in range(grid.shape[1]) if grid[x][y] == EMPTY]

        for x in range(grid.shape[0]):
            for y in range(grid.shape[1]):
                if is_unsatisfied(grid, x, y, tolerance):
                    unsatisfied.append((x, y))

        if not unsatisfied:
            print("Equilibrium met at", it, "iterations.")
            break

        random.shuffle(unsatisfied)
        for x, y in unsatisfied:
            relocate(grid, x, y, empty_cells)

        print("Current iteration: ", it)
        plot_grid(grid)

    return grid

def plot_grid(grid):
    color_map = {EMPTY: [0, 0, 0], RED: [1, 0, 0], GREEN: [0, 1, 0]}
    rgb_array = np.zeros((grid.shape[0], grid.shape[1], 3))
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            rgb_array[x, y] = color_map[grid[x, y]]
    plt.imshow(rgb_array)
    plt.axis('off')
    plt.show()

# Główna symulacja
grid = create_grid(size, empty_ratio)
plot_grid(grid)
grid = simulate(grid, tolerance, max_iters)
plot_grid(grid)