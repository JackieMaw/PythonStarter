import matplotlib.pyplot as plt
import numpy as np
import heapq
import matplotlib.colors as mcolors  # ✅ Fix: Import colors properly

def load_labyrinth(filename="labyrinth.txt"):
    """Loads the labyrinth from a text file."""
    with open(filename, "r") as f:
        lines = f.readlines()

    # Read dimensions
    num_rows = len(lines)
    num_cols = len(lines[0].strip())

    # Convert the labyrinth into a matrix for visualization
    grid = [list(line.strip()) for line in lines]
    return np.array(grid)

def dijkstra(grid):
    """Finds the shortest path in the labyrinth using Dijkstra's algorithm."""
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

    # Movement directions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    costs = {'.': 1, 'S': 1, 'E': 1, '$': 0.5, 'T': 3, 'K': 1, 'D': 1, '#': float('inf')}

    while pq:
        current_cost, (x, y) = heapq.heappop(pq)

        if (x, y) == end:
            break  # Found the exit

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                new_cost = current_cost + costs.get(grid[nx, ny], float('inf'))
                if new_cost < distances.get((nx, ny), float('inf')):
                    distances[(nx, ny)] = new_cost
                    heapq.heappush(pq, (new_cost, (nx, ny)))
                    previous_nodes[(nx, ny)] = (x, y)

    # Backtrack to get the shortest path
    path = []
    current = end
    while current in previous_nodes:
        path.append(current)
        current = previous_nodes[current]
    path.append(start)
    return path

def visualize_labyrinth(grid, path=None):
    """Visualizes the labyrinth and highlights the shortest path."""
    n, m = grid.shape

    # Create a color map for different elements
    color_map = {
        '#': 'black',   # Walls
        '.': 'white',   # Path
        'S': 'blue',    # Start
        'E': 'green',   # Exit
        'T': 'red',     # Traps
        '$': 'gold',    # Treasure
        'K': 'purple',  # Key
        'D': 'brown'    # Door
    }

    # Create an empty image
    img = np.zeros((n, m, 3))

    for i in range(n):
        for j in range(m):
            color = mcolors.to_rgb(color_map.get(grid[i, j], 'white'))  # ✅ Fix: Use mcolors.to_rgb()
            img[i, j] = color

    # Highlight the shortest path
    if path:
        for x, y in path:
            img[x, y] = mcolors.to_rgb('cyan')  # ✅ Fix: Use mcolors.to_rgb() for cyan path

    # Plot the labyrinth
    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    plt.xticks([])  # Remove X ticks
    plt.yticks([])  # Remove Y ticks
    plt.title("Labyrinth with Shortest Path")
    plt.show()

# Load labyrinth
grid = load_labyrinth()

# Find the shortest path
shortest_path = dijkstra(grid)

# Visualize the labyrinth with the path
visualize_labyrinth(grid, shortest_path)