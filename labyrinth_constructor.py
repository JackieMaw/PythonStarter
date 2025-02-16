import random
from visualization import initialize_visualization, visualize_labyrinth, show_visualization

def generate_labyrinth(n=100, m=100, trap_percent=10, treasure_percent=10, extra_paths=200):
    """Generates a labyrinth with multiple paths, traps (T), and treasures ($)."""
    
    # Initialize grid with walls
    grid = [['#' for _ in range(m)] for _ in range(n)]

    visualize_labyrinth(grid, init=False, pause=0.01)

    # Random starting point
    # start_x, start_y = random.randrange(1, n-1, 2), random.randrange(1, m-1, 2)
    start_x = 1
    start_y = 1
    grid[start_x][start_y] = 'S'  # Mark start position    

    visualize_labyrinth(grid, init=False, pause=0.01)

    # List of wall candidates
    walls = [(start_x + dx, start_y + dy) for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]
             if 0 < start_x + dx < n-1 and 0 < start_y + dy < m-1]

    random.shuffle(walls)

    while walls:
        x, y = walls.pop()
        if grid[x][y] == '#':  # Only process if still a wall
            # Find neighbors that are paths
            neighbors = [(x + dx, y + dy) for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]
                         if 0 < x + dx < n-1 and 0 < y + dy < m-1 and grid[x + dx][y + dy] in ('.', 'S')]

            if neighbors:
                nx, ny = random.choice(neighbors)  # Pick a random connected path
                grid[x][y] = '.'  # Open current cell
                grid[(x + nx) // 2][(y + ny) // 2] = '.'  # Open passage
                visualize_labyrinth(grid, init=False, pause=0.01)

                # Add new walls to the list
                walls.extend([(x + dx, y + dy) for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]
                              if 0 < x + dx < n-1 and 0 < y + dy < m-1 and grid[x + dx][y + dy] == '#'])
                random.shuffle(walls)

    # Place exit in the bottom-right corner
    exit_x, exit_y = n - 2, m - 2
    grid[exit_x][exit_y] = 'E'
    visualize_labyrinth(grid, init=False, pause=0.01)

    # **Extra Step: Add random paths to create multiple routes**
    for _ in range(extra_paths):
        rx, ry = random.randrange(1, n-1, 2), random.randrange(1, m-1, 2)
        if grid[rx][ry] == '#':  # Carve out additional paths
            grid[rx][ry] = '.'
            # Ensure it connects to an existing path
            neighbors = [(rx + dx, ry + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                         if 0 < rx + dx < n-1 and 0 < ry + dy < m-1 and grid[rx + dx][ry + dy] == '.']
            if neighbors:
                nx, ny = random.choice(neighbors)
                grid[(rx + nx) // 2][(ry + ny) // 2] = '.'
            
            visualize_labyrinth(grid, init=False, pause=0.01)

    # Add monsters ('M') and potions ('*')
    empty_cells = [(x, y) for x in range(n) for y in range(m) if grid[x][y] == '.']
    num_traps = len(empty_cells) * trap_percent // 100
    num_treasures = len(empty_cells) * treasure_percent // 100

    for x, y in random.sample(empty_cells, num_traps):
        grid[x][y] = 'M'  # Monster
        visualize_labyrinth(grid, init=False, pause=0.01)

    for x, y in random.sample(empty_cells, num_treasures):
        grid[x][y] = '*'  # Potion
        visualize_labyrinth(grid, init=False, pause=0.01)

    return grid

def save_labyrinth(grid, filename):
    """Saves the labyrinth to a text file."""
    with open(filename, "w") as f:
        for row in grid:
            f.write("".join(row) + "\n")

# Generate and save the labyrinth
n=21
m=21
initialize_visualization()
labyrinth = generate_labyrinth(n, m)
filename = f"labyrinth_{n}x{m}.txt"
save_labyrinth(labyrinth, filename)
print(f"✅ Labyrinth with multiple paths, traps & treasures saved to '{filename}'!")
show_visualization()
