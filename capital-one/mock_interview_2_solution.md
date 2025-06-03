# Capital One Mock Interview Set 2: 2D Matrix & Simulation

*Focus: Matrix manipulation, pathfinding, and grid-based problems*

## ⏱️ Time Allocation: 45 minutes total
- **Question 1**: 8 minutes (Easy)
- **Question 2**: 10 minutes (Easy-Medium) 
- **Question 3**: 12 minutes (Medium)
- **Question 4**: 15 minutes (Medium-Hard)

---

## Question 1 (Easy - Matrix Basics)

You are given a rectangular matrix of integers `grid` and need to convert it into a "normalized" matrix where each cell contains the count of non-zero neighbors (including diagonally adjacent cells). A cell cannot count itself as a neighbor.

For `grid = [[1, 0, 3], [2, 5, 0], [0, 1, 4]]`, the output should be:
```
[[2, 3, 1],
 [3, 4, 3], 
 [2, 3, 2]]
```

Your task is to return the normalized matrix.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(grid.length × grid[0].length)² will fit within the execution time limit.

### Pattern Recognition
- **Type**: Matrix Traversal with Neighbor Counting
- **Template**: 2D Matrix Template with 8-directional movement

### Solution Approach
```python
def normalize_matrix(grid):
    if not grid or not grid[0]:
        return []
    
    rows, cols = len(grid), len(grid[0])
    result = [[0] * cols for _ in range(rows)]
    
    # 8-directional neighbors (including diagonals)
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    for r in range(rows):
        for c in range(cols):
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc) and grid[nr][nc] != 0:
                    count += 1
            result[r][c] = count
    
    return result
```

---

## Question 2 (Medium - Matrix Transformation)

Imagine that you are implementing a game board rotation system. Given a square matrix `board` representing a game board, you need to perform the following operations in sequence:

1. Rotate the matrix 90 degrees clockwise
2. Reflect the matrix horizontally (flip left-right)
3. Swap the values of each row with its corresponding column (transpose)

Your task is to return the final transformed matrix after applying all three operations.

**Example**: For `board = [[1, 2], [3, 4]]`, after all transformations, the output should be the final matrix state.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(board.length³) will fit within the execution time limit.

### Pattern Recognition
- **Type**: Matrix Transformation Sequence
- **Template**: Matrix Manipulation with Multiple Operations

### Solution Approach
```python
def transform_board(board):
    if not board or not board[0]:
        return []
    
    n = len(board)
    result = [row[:] for row in board]  # Deep copy
    
    # Step 1: Rotate 90 degrees clockwise
    result = rotate_clockwise(result)
    
    # Step 2: Reflect horizontally (flip left-right)
    result = reflect_horizontal(result)
    
    # Step 3: Transpose
    result = transpose(result)
    
    return result

def rotate_clockwise(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = matrix[i][j]
    return rotated

def reflect_horizontal(matrix):
    return [row[::-1] for row in matrix]

def transpose(matrix):
    n = len(matrix)
    transposed = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transposed[j][i] = matrix[i][j]
    return transposed
```

---

## Question 3 (Medium - Pathfinding with Constraints)

You are given a matrix `warehouse` consisting of 0s and 1s, where 0 represents an empty space and 1 represents an obstacle. You need to find the shortest path from the top-left corner `(0, 0)` to the bottom-right corner `(m-1, n-1)`, but with a special constraint: you can "break through" at most 2 obstacles during your journey.

The robot can move in 4 directions (up, down, left, right) and each move has a cost of 1. Breaking through an obstacle also costs 1 move. If no path exists even with breaking through 2 obstacles, return -1.

Your task is to return the minimum number of moves required to reach the destination.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(warehouse.length × warehouse[0].length)³ will fit within the execution time limit.

### Pattern Recognition
- **Type**: BFS with State Tracking (obstacles broken)
- **Template**: Modified BFS with 3D visited array

### Solution Approach
```python
from collections import deque

def shortest_path_with_obstacles(warehouse):
    if not warehouse or not warehouse[0]:
        return -1
    
    rows, cols = len(warehouse), len(warehouse[0])
    if warehouse[0][0] == 1 or warehouse[rows-1][cols-1] == 1:
        return -1
    
    # BFS with state: (row, col, obstacles_broken, steps)
    queue = deque([(0, 0, 0, 0)])  # start at (0,0) with 0 obstacles broken, 0 steps
    visited = set([(0, 0, 0)])  # (row, col, obstacles_broken)
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        r, c, broken, steps = queue.popleft()
        
        # Check if reached destination
        if r == rows - 1 and c == cols - 1:
            return steps
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                new_broken = broken
                
                # If it's an obstacle, we need to break it
                if warehouse[nr][nc] == 1:
                    new_broken += 1
                
                # Only proceed if we haven't broken too many obstacles
                if new_broken <= 2 and (nr, nc, new_broken) not in visited:
                    visited.add((nr, nc, new_broken))
                    queue.append((nr, nc, new_broken, steps + 1))
    
    return -1
```
```python
# Test case 1: Simple path with obstacles
warehouse1 = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

# Test case 2: Path requiring breaking obstacles
warehouse2 = [
    [0, 1, 1],
    [0, 1, 0],
    [0, 0, 0]
]

# Test case 3: No possible path
warehouse3 = [
    [0, 1, 1],
    [1, 1, 1],
    [1, 1, 0]
]

# Test your function
print(find_shortest_path(warehouse1, 2))  # Should find a path
print(find_shortest_path(warehouse2, 2))  # Should find a path breaking 1-2 obstacles
print(find_shortest_path(warehouse3, 2))  # Should return -1 (no path possible)
```
---

## Question 4 (Hard - Matrix Simulation)

Given a matrix of integers `colors` representing a puzzle game board, you need to simulate a "cascade elimination" system. When a user clicks on a cell at position `[r, c]`, the following happens:

1. If the cell is empty (value 0), nothing happens
2. If the cell contains a color (non-zero value), all connected cells with the same color are eliminated (set to 0)
3. Connected means 4-directionally adjacent (not diagonal)
4. After elimination, gravity applies: all remaining colors "fall down" to fill empty spaces
5. This process repeats until no more eliminations are possible

Given the initial `colors` matrix and an array `clicks` representing user click positions `[r, c]`, your task is to return the final state of the matrix after all clicks and cascading eliminations.

**Example**: For `colors = [[1, 1, 2], [1, 2, 2], [3, 2, 1]]` and `clicks = [[0, 0]]`, simulate the elimination and gravity effects.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(colors.length × colors[0].length)³ will fit within the execution time limit.

### Pattern Recognition
- **Type**: Matrix Simulation with DFS and Gravity
- **Template**: DFS + Matrix Transformation

### Solution Approach
```python
def cascade_elimination(colors, clicks):
    if not colors or not colors[0]:
        return colors
    
    rows, cols = len(colors), len(colors[0])
    matrix = [row[:] for row in colors]  # Deep copy
    
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    def dfs_eliminate(r, c, target_color, visited):
        if not is_valid(r, c) or visited[r][c] or matrix[r][c] != target_color:
            return
        
        visited[r][c] = True
        matrix[r][c] = 0  # Eliminate
        
        # Check 4 directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            dfs_eliminate(r + dr, c + dc, target_color, visited)
    
    def apply_gravity():
        # For each column, move all non-zero elements down
        for c in range(cols):
            # Collect non-zero elements from bottom to top
            non_zero = []
            for r in range(rows - 1, -1, -1):
                if matrix[r][c] != 0:
                    non_zero.append(matrix[r][c])
            
            # Clear the column
            for r in range(rows):
                matrix[r][c] = 0
            
            # Place non-zero elements from bottom
            for i, val in enumerate(non_zero):
                matrix[rows - 1 - i][c] = val
    
    def has_groups():
        # Check if there are any groups of connected same-color cells
        visited = [[False] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and matrix[r][c] != 0:
                    # Count connected cells of same color
                    count = count_connected(r, c, matrix[r][c], visited)
                    if count > 1:
                        return True
        return False
    
    def count_connected(r, c, color, visited):
        if not is_valid(r, c) or visited[r][c] or matrix[r][c] != color:
            return 0
        
        visited[r][c] = True
        count = 1
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            count += count_connected(r + dr, c + dc, color, visited)
        
        return count
    
    # Process each click
    for click_r, click_c in clicks:
        if is_valid(click_r, click_c) and matrix[click_r][click_c] != 0:
            target_color = matrix[click_r][click_c]
            visited = [[False] * cols for _ in range(rows)]
            dfs_eliminate(click_r, click_c, target_color, visited)
            
            # Apply gravity and continue eliminating until no more groups
            while True:
                apply_gravity()
                if not has_groups():
                    break
                
                # Eliminate all groups
                visited = [[False] * cols for _ in range(rows)]
                for r in range(rows):
                    for c in range(cols):
                        if not visited[r][c] and matrix[r][c] != 0:
                            color = matrix[r][c]
                            if count_connected(r, c, color, [[False] * cols for _ in range(rows)]) > 1:
                                dfs_eliminate(r, c, color, visited)
    
    return matrix
```

---

## 🎯 Key Takeaways for Set 2

1. **Matrix Navigation**: Master 4-directional and 8-directional movement
2. **State Tracking**: Use visited arrays and maintain game state
3. **Transformation Sequences**: Apply operations step by step
4. **BFS with Constraints**: Track additional state in queue
5. **Simulation Logic**: Handle complex multi-step processes
6. **Gravity Effects**: Implement column-wise element movement
