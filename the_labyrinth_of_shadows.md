### **The Labyrinth of Shadows**  

#### **Story**  
You are an adventurer trapped in the **Labyrinth of Shadows**, an underground maze filled with dangerous monsters and magic potions. You can feel the ground trembling and you fear that the labyrinth will collapse soon. Your goal is to escape the labyrinth **as soon as possible**. Can you find the quickest way out whilst avoiding monsters and drinking as many magic potions as you can? Get started now because time is running out!

#### **Game Rules**  
- The labyrinth is represented as a **grid (N x M)** where each cell has a **cost** (representing the time it will take you).  
- You start at the **top-left corner** and must reach the **bottom-right corner**.  
- Each cell contains one of the following:  
  - **Empty Path (.)** → Normal cost = 1 minute  
  - **Wall (#)** → Impassable  
  - **Monster (M)** → High cost = 5 minutes
  - **Magic Potion (*)** → No cost = 0 minutes
- You can **only move up, down, left, or right**.  
#### **Example Input**  
```
#####
#S..#
#.#.#
#M.E#
##### 
```
(S = Start, E = Exit)  

#### **Solution Approach**  
- Model the grid as a **weighted graph** where each cell is a node.  
- Use **Dijkstra’s algorithm** to find the shortest-cost path while considering:  
  - **Monsters(M) increase cost.**  
  - **Magic Potions(*) have no cost.**