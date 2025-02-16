import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors 

def initialize_visualization():
    plt.figure(figsize=(10, 10))

def show_visualization():
    plt.show()

def visualize_labyrinth(labyrinth, path=None, init=True, pause=0):

    grid = np.array(labyrinth)
    n, m = grid.shape

    # Create a color map for different elements
    color_map = {
        '#': 'black',   # Walls
        '.': 'white',   # Path
        'S': 'blue',    # Start
        'E': 'green',   # Exit
        'M': 'red',     # Monster
        '*': 'gold',    # Potion
        'K': 'purple',  # Key
        'D': 'brown'    # Door
    }

    # Create an empty image
    img = np.zeros((n, m, 3))

    for i in range(n):
        for j in range(m):
            color = mcolors.to_rgb(color_map.get(grid[i, j], 'white'))
            img[i, j] = color

    # Highlight the shortest path
    if path:
        for x, y in path:
            img[x, y] = mcolors.to_rgb('cyan')

    # Plot the labyrinth
    if init:
        initialize_visualization()
    plt.imshow(img)
    plt.xticks([])  # Remove X ticks
    plt.yticks([])  # Remove Y ticks
    plt.title("The Labyrinth of Shadows")
    if pause > 0:
        plt.pause(pause)
    else:
        plt.show()