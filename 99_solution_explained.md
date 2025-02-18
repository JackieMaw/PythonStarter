Here's a **Python implementation** of the **Labyrinth of Shadows** challenge using **Dijkstra's algorithm**.  

---

### **Solution Approach**  
- The labyrinth is treated as a **graph** where each cell is a **node**.  
- We use **Dijkstra’s algorithm** to find the path with the **minimum cost** from the **start (S)** to the **exit (E)**.  
- **Monsters (M) increase cost**, **magic potions (*) reduce cost**, and **walls (#) block movement**.  
- **Keys (K) must be collected to pass doors (D)**.  

---

### **How It Works**  
1. **Parses the labyrinth grid from input.**  
2. **Uses a priority queue** (`heapq`) to always expand the lowest-cost path first.  
3. **Handles monsters (M) and magic potions (*) by modifying costs.**  
4. **Manages keys (K) and doors (D)** so that doors are only passable once a key is collected.  
5. **Returns the minimum cost to escape.**  

---

### **Example Run**  
#### **Input**  
```
#####
#S..#
#.#.#
#M.E#
#####df31
```
#### **Output**  
```
7
```

---

### **Possible Extensions**
- Add **moving enemies** that change the shortest path dynamically.  
- Introduce **multiple exits**, each offering a different reward.  
- Add **time-based elements**, where the dungeon collapses after a set number of moves.