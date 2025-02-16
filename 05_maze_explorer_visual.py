import matplotlib.pyplot as plt
import numpy as np
import heapq
import time
import matplotlib.colors as mcolors
from loader import load_labyrinth
from visualization import visualize_labyrinth

def dijkstra(grid, visualize=True):
    """Finds the shortest path in the labyrinth using Dijkstra’s algorithm with step visualization."""
    n, m = grid.shape
    start, end = None, None

    # Locate the start and exit positions
    for i in range(n):
        for j in range(m):
            if grid[i, j] == 'S':
                start = (i, j)
            elif grid[i, j] == 'E':
                end = (i, j)

    if not start or not end:
        raise ValueError("Labyrinth must contain both 'S' (start) and 'E' (exit).")

    # Dijkstra's priority queue
    pq = [(0, start)]  # (cost, (x, y))
    distances = {start: 0}
    previous_nodes = {}
    visited = set()

    # Movement directions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Custom movement costs
    costs = {
        '.': 1,   # Normal path
        'S': 1,   # Start
        'E': 1,   # Exit
        '$': 0.5, # Treasure (reduces cost)
        'T': 3,   # Trap (increases cost)
        '#': float('inf')  # Walls (impassable)
    }

    plt.figure(figsize=(10, 10))  # Set figure size

    while pq:
        current_cost, (x, y) = heapq.heappop(pq)

        if (x, y) == end:
            break  # Found the exit

        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                new_cost = current_cost + costs.get(grid[nx, ny], float('inf'))
                if new_cost < distances.get((nx, ny), float('inf')):
                    distances[(nx, ny)] = new_cost
                    heapq.heappush(pq, (new_cost, (nx, ny)))
                    previous_nodes[(nx, ny)] = (x, y)

        # **Visualize each step**
        if visualize:
            visualize_labyrinth(grid, visited=visited)

    # Backtrack to get the shortest path
    path = []
    current = end
    while current in previous_nodes:
        path.append(current)
        current = previous_nodes[current]
    path.append(start)
    path.reverse()

    # Final visualization with the shortest path
    visualize_labyrinth(grid, path=path, visited=visited)
    plt.show()  # Ensure the last step is visible
    return path

# Load labyrinth
grid = load_labyrinth()

# Find the shortest path and visualize every step
shortest_path = dijkstra(grid, visualize=True)

print("✅ Shortest path found! Visualized step by step.")
