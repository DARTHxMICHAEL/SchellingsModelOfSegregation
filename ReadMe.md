# Schelling's Model of Segregation (Python Implementation)

This project implements a simple simulation of **Schelling's Model of Segregation** using Python, NumPy, and Matplotlib.

The model demonstrates how **local preferences of agents can lead to large-scale spatial segregation**, even when those preferences are relatively weak.

## Model Description

The simulation runs on a 2D grid where each cell can contain:

- **RED agent**
- **GREEN agent**
- **EMPTY cell**

Agents evaluate their neighborhood and decide whether they are satisfied with their current location. If the proportion of neighbors of a different type exceeds a defined **tolerance threshold**, the agent relocates to a random empty cell.

The simulation continues until:

- all agents are satisfied (equilibrium), or
- the maximum number of iterations is reached.

## Parameters

The main parameters of the model are:

| Parameter | Description |
|--------|--------|
| `size` | Size of the grid (size × size) |
| `empty_ratio` | Fraction of empty cells in the grid |
| `tolerance` | Maximum tolerated proportion of different neighbors |
| `max_iters` | Maximum number of simulation iterations |

Default values in the code:

```
size = 200
empty_ratio = 0.1
tolerance = 0.20
max_iters = 500
```

## Simulation Rules

1. Agents observe their **Moore neighborhood** (8 surrounding cells).
2. Empty cells are ignored when calculating similarity.
3. If the fraction of different neighbors exceeds `tolerance`, the agent becomes **unsatisfied**.
4. Unsatisfied agents relocate to a **random empty cell**.
5. The process repeats until equilibrium is reached.

## Visualization

The grid is visualized using Matplotlib:

- **Red** → RED agents  
- **Green** → GREEN agents  
- **Black** → Empty cells  

The simulation displays the grid after each iteration.

## Requirements

Install the required Python libraries:

```bash
pip install numpy matplotlib
```

## Running the Simulation

Run the script:

```bash
python main.py
```

The program will:

1. Generate a random initial population.
2. Display the starting grid.
3. Run the simulation.
4. Display intermediate steps.
5. Show the final equilibrium state.

## Purpose

This implementation is intended for:

- studying **emergent segregation**
- demonstrating **agent-based modeling**
- educational use in **complex systems and social simulation**

## References

Thomas C. Schelling (1971)  
*Dynamic Models of Segregation*  
Journal of Mathematical Sociology