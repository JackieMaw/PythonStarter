def load_labyrinth(filename="labyrinth.txt"):
    
    with open(filename, "r") as f:
        lines = f.readlines()

    labyrinth = [list(line.strip()) for line in lines]
    return labyrinth