import heapq

def load_labyrinth(filename="labyrinth.txt"):
    """Loads the labyrinth from a text file."""
    with open(filename, "r") as f:
        lines = f.readlines()

    # Read dimensions
    num_rows = len(lines)
    num_cols = len(lines[0].strip())

    # Convert the labyrinth into a matrix for visualization
    grid = [list(line.strip()) for line in lines]
    return grid, num_rows, num_cols

def dijkstra(labyrinth, start, end, n, m):
    # Movement directions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Cost dictionary for different cell types
    cell_cost = {'.': 1, 'T': 5, '$': 1, '#': float('inf'), 'K': 1, 'D': float('inf'), 'S': 1, 'E': 1}
    
    # Priority queue for Dijkstra (cost, x, y, keys_collected)
    pq = [(0, start[0], start[1], False)]  # (cost, x, y, has_key)
    
    # Distance dictionary (cost, has_key state)
    dist = {}
    dist[(start[0], start[1], False)] = 0
    
    while pq:
        cost, x, y, has_key = heapq.heappop(pq)
        
        # If reached exit, return the cost
        if (x, y) == end:
            return cost
        
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                cell = labyrinth[nx][ny]
                new_cost = cost + cell_cost.get(cell, 1)
                
                # Collect treasure (reduce cost)
                if cell == '$':
                    new_cost -= 3  # Treasure reduces cost
                
                # Pick up key
                new_has_key = has_key or (cell == 'K')
                
                # Doors can only be passed if we have a key
                if cell == 'D' and not new_has_key:
                    continue
                
                # Update distance
                state = (nx, ny, new_has_key)
                if state not in dist or new_cost < dist[state]:
                    dist[state] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny, new_has_key))
    
    return -1  # No path found

labyrinth, n, m = load_labyrinth()
print(f"{n}x{m}")
print(labyrinth)

# Find start and exit positions
start, end = None, None
for i in range(n):
    for j in range(m):
        if labyrinth[i][j] == 'S':
            start = (i, j)
        elif labyrinth[i][j] == 'E':
            end = (i, j)

# Run Dijkstra's algorithm and print result
print(dijkstra(labyrinth, start, end, n, m))