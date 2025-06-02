## 🎯 Mock Interview Set 2: **2D Matrix & Simulation**
*Focus: Matrix manipulation, pathfinding, and grid-based problems*

### **Question 1 (Easy - Matrix Basics)**
You are given a rectangular matrix of integers `grid` and need to convert it into a "normalized" matrix where each cell contains the count of non-zero neighbors (including diagonally adjacent cells). A cell cannot count itself as a neighbor.

For `grid = [[1, 0, 3], [2, 5, 0], [0, 1, 4]]`, the output should be:
```
[[2, 4, 1],
 [3, 5, 4], 
 [3, 3, 2]]
```

Your task is to return the normalized matrix.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(grid.length × grid[0].length)² will fit within the execution time limit.

---

### **Question 2 (Medium - Matrix Transformation)**
Imagine that you are implementing a game board rotation system. Given a square matrix `board` representing a game board, you need to perform the following operations in sequence:

1. Rotate the matrix 90 degrees clockwise
2. Reflect the matrix horizontally (flip left-right)
3. Swap the values of each row with its corresponding column (transpose)

Your task is to return the final transformed matrix after applying all three operations.

**Example**: For `board = [[1, 2], [3, 4]]`, after all transformations, the output should be the final matrix state.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(board.length³) will fit within the execution time limit.

---

### **Question 3 (Medium - Pathfinding with Constraints)**
You are given a matrix `warehouse` consisting of 0s and 1s, where 0 represents an empty space and 1 represents an obstacle. You need to find the shortest path from the top-left corner `(0, 0)` to the bottom-right corner `(m-1, n-1)`, but with a special constraint: you can "break through" at most 2 obstacles during your journey.

The robot can move in 4 directions (up, down, left, right) and each move has a cost of 1. Breaking through an obstacle also costs 1 move. If no path exists even with breaking through 2 obstacles, return -1.

Your task is to return the minimum number of moves required to reach the destination.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(warehouse.length × warehouse[0].length)³ will fit within the execution time limit.

---

### **Question 4 (Hard - Matrix Simulation)**
Given a matrix of integers `colors` representing a puzzle game board, you need to simulate a "cascade elimination" system. When a user clicks on a cell at position `[r, c]`, the following happens:

1. If the cell is empty (value 0), nothing happens
2. If the cell contains a color (non-zero value), all connected cells with the same color are eliminated (set to 0)
3. Connected means 4-directionally adjacent (not diagonal)
4. After elimination, gravity applies: all remaining colors "fall down" to fill empty spaces
5. This process repeats until no more eliminations are possible

Given the initial `colors` matrix and an array `clicks` representing user click positions `[r, c]`, your task is to return the final state of the matrix after all clicks and cascading eliminations.

**Example**: For `colors = [[1, 1, 2], [1, 2, 2], [3, 2, 1]]` and `clicks = [[0, 0]]`, simulate the elimination and gravity effects.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(colors.length × colors[0].length)³ will fit within the execution time limit.

---