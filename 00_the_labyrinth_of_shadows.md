### **Game Challenge: The Labyrinth of Shadows**  

#### **Story**  
You are an adventurer trapped in the **Labyrinth of Shadows**, a dungeon filled with traps, locked doors, and treasures. Your goal is to escape the labyrinth **with the most treasure** while avoiding deadly traps.  

#### **Game Rules**  
- The labyrinth is represented as a **grid (N x M)** where each cell has a **cost** (representing danger or difficulty).  
- You start at the **top-left corner** and must reach the **bottom-right corner**.  
- Each cell contains:  
  - **Empty Path (.)** → Low cost (1)  
  - **Wall (#)** → Impassable  
  - **Trap (T)** → High cost (5-10)  
  - **Treasure ($)** → Reduces total cost (-3 per treasure)  
  - **Keys (K) and Doors (D)** → You must collect a key before passing a door  
- You can **only move up, down, left, or right**.  

#### **Input Format**  
1. **First Line:** Two integers **N** and **M** (size of the grid).  
2. **Next N Lines:** A string of length M representing the grid.  
3. **Treasure Cells Count:** An integer **X** (number of treasure cells).  
4. **Trap Cells Count:** An integer **Y** (number of traps).  

#### **Example Input**  
```
5 5  
S..T.  
.#.#.  
.K.$D  
...$.  
...E  
```
(S = Start, E = Exit)  

#### **Output Format**  
- The **minimum cost** to escape while collecting treasure.  

#### **Example Output**  
```
7  
```  

#### **Solution Approach**  
- Model the grid as a **weighted graph** where each cell is a node.  
- Use **Dijkstra’s algorithm** to find the shortest-cost path while considering:  
  - **Traps increase cost.**  
  - **Treasure reduces cost.**  
  - **Keys are needed to pass doors.**  