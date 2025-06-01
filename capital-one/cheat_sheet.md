# Capital One Interview Preparation: 2D Matrix & Greedy Algorithm Cheat Sheets

*Generated from GitHub Copilot Chat conversation on 2025-06-01*

## Overview

This document contains comprehensive cheat sheets and problem-solving strategies for Capital One technical interviews, focusing on 2D matrix problems and greedy algorithms with practical implementations.

## 📋 Table of Contents

1. [2D Matrix Cheat Sheet](#2d-matrix-cheat-sheet)
2. [Greedy Algorithm Cheat Sheet](#greedy-algorithm-cheat-sheet)
3. [Solved Problems](#solved-problems)
   - [Fishing Problem (Greedy Resource Matching)](#fishing-problem)
   - [Memory Allocation Problem](#memory-allocation-problem)
   - [Array Query Processing](#array-query-processing)
   - [Rating System Problem](#rating-system-problem)

---

## 🔥 2D Matrix Cheat Sheet for Capital One

### Essential Starter Code Template

```python
def matrix_template(matrix):
    if not matrix or not matrix[0]:
        return []  # Handle edge cases
    
    rows, cols = len(matrix), len(matrix[0])
    
    # Common patterns:
    # 1. Initialize result/visited arrays
    result = []
    visited = [[False] * cols for _ in range(rows)]
    
    # 2. Direction arrays for movement
    directions = [(0,1), (1,0), (0,-1), (-1,0)]  # right, down, left, up
    
    # 3. Boundary check function
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    # 4. DFS/BFS helper (choose based on problem)
    def dfs(r, c):
        if not is_valid(r, c) or visited[r][c]:
            return
        visited[r][c] = True
        # Process current cell
        for dr, dc in directions:
            dfs(r + dr, c + dc)
    
    return result
```

### Top 15 Capital One Matrix Questions to Master

**Easy (Must Know)**
1. **Spiral Matrix** - LeetCode 54
2. **Search 2D Matrix** - LeetCode 74
3. **Set Matrix Zeroes** - LeetCode 73
4. **Transpose Matrix** - LeetCode 867

**Medium (High Priority)**
5. **Rotate Image** - LeetCode 48
6. **Word Search** - LeetCode 79
7. **Number of Islands** - LeetCode 200
8. **Unique Paths** - LeetCode 62
9. **Minimum Path Sum** - LeetCode 64
10. **Search 2D Matrix II** - LeetCode 240
11. **Game of Life** - LeetCode 289

**Medium-Hard (Capital One Favorites)**
12. **Longest Increasing Path in Matrix** - LeetCode 329
13. **Surrounded Regions** - LeetCode 130
14. **Pacific Atlantic Water Flow** - LeetCode 417
15. **Max Area of Island** - LeetCode 695

### Quick Reference Patterns

```python
# Direction Arrays
dirs = [(0,1), (1,0), (0,-1), (-1,0)]  # 4-directional
dirs = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]  # 8-directional

# Common Edge Cases
if not matrix or not matrix[0]: return []
if len(matrix) == 1: # handle single row
if len(matrix[0]) == 1: # handle single column

# Boundary Check Function
def is_valid(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols
```

---

## 🔥 Greedy Algorithm Cheat Sheet for Capital One

### Essential Starter Code Template

```python
def greedy_template(items):
    # Step 1: Handle edge cases
    if not items:
        return []
    
    # Step 2: Sort by greedy criteria (most important step!)
    items.sort(key=lambda x: x.priority, reverse=True)  # or False
    
    # Step 3: Initialize tracking variables
    result = []
    used = set()  # or counter/visited array
    
    # Step 4: Greedy selection loop
    for item in items:
        if is_valid(item, used):
            result.append(item)
            used.add(item)  # update state
            
            # Optional: early termination
            if len(result) == target_size:
                break
    
    return result
```

### Capital One Specific Templates

#### Template 1: Resource Matching (Fish & Bait Pattern)
```python
def resource_matching_template(resources, tools):
    """For problems like fish-bait, job-workers, etc."""
    if not resources or not tools:
        return 0
    
    # Sort both by size/capability (largest first usually optimal)
    resources.sort(reverse=True)
    tools.sort(reverse=True)
    
    matches = 0
    used_resources = []
    
    for tool in tools:
        tool_uses = 0
        max_uses = get_max_uses(tool)  # e.g., 3 for bait
        
        while tool_uses < max_uses and resources:
            # Find best resource this tool can handle
            best_idx = find_best_match(tool, resources)
            if best_idx != -1:
                matches += 1
                resources.pop(best_idx)
                tool_uses += 1
            else:
                break
    
    return matches
```

#### Template 2: Query Processing with Updates
```python
def query_processing_template(initial_data, queries):
    """For problems with mixed read/write operations"""
    data = initial_data.copy()
    results = []
    
    for query in queries:
        query_type = query[0]
        
        if query_type == 0:  # Update operation
            idx, value = query[1], query[2]
            data[idx] += value  # or other update logic
            
        elif query_type == 1:  # Query operation
            target = query[1]
            result = process_query(data, target)
            results.append(result)
    
    return results
```

#### Template 3: Interval/Memory Allocation
```python
def interval_allocation_template(size, operations):
    """For memory allocation, scheduling problems"""
    memory = [0] * size  # 0 = free, 1 = occupied
    allocated_blocks = {}  # track allocations
    
    for op in operations:
        if op[0] == "alloc":
            block_size = op[1]
            start_pos = find_leftmost_free_block(memory, block_size)
            if start_pos != -1:
                allocate_block(memory, start_pos, block_size)
                allocated_blocks[start_pos] = block_size
                
        elif op[0] == "erase":
            index = op[1]
            if index in allocated_blocks:
                block_size = allocated_blocks[index]
                free_block(memory, index, block_size)
                del allocated_blocks[index]
    
    return memory
```

#### Template 4: Rating/Level Systems
```python
def rating_system_template(initial_rating, changes):
    """For rating updates with level classifications"""
    current_rating = initial_rating
    
    # Define level thresholds
    levels = [(1, "beginner"), (1000, "intermediate"), 
              (1500, "advanced"), (2000, "pro")]
    
    # Process changes greedily
    for change in changes:
        current_rating += change
        # Clamp if needed
        current_rating = max(1, min(2500, current_rating))
    
    # Determine final level
    for threshold, level in reversed(levels):
        if current_rating >= threshold:
            return level
    
    return levels[0][1]  # fallback
```

---

## 🎯 Solved Problems

### 1. Fishing Problem (Greedy Resource Matching)

**Problem**: Given arrays of fish sizes and bait sizes, where bait must be strictly smaller than fish, each bait can be used up to 3 times, find maximum fish that can be caught.

**Pattern Recognition**: Greedy Algorithm with Resource Constraints

**Solution**:
```python
def max_fish_caught(fish, baits):
    if not fish or not baits:
        return 0
    
    # Sort baits largest to smallest (greedy: use largest bait first)
    baits.sort(reverse=True)
    available_fish = sorted(fish, reverse=True)
    
    caught_count = 0
    
    for bait_size in baits:
        bait_uses = 0  # Track uses for current bait (max 3)
        
        while bait_uses < 3 and available_fish:
            # Find largest fish that this bait can catch
            caught_fish_idx = -1
            
            for i, fish_size in enumerate(available_fish):
                if bait_size < fish_size:  # Bait must be strictly smaller
                    caught_fish_idx = i
                    break
            
            if caught_fish_idx != -1:
                available_fish.pop(caught_fish_idx)
                caught_count += 1
                bait_uses += 1
            else:
                break
    
    return caught_count
```

**Time Complexity**: O(B × F) where B = baits, F = fish

---

### 2. Memory Allocation Problem

**Problem**: Implement memory allocator with alloc (find leftmost free block) and erase operations.

**Pattern Recognition**: Greedy + Simulation with State Tracking

**Solution**:
```python
def solve_memory_queries(memory, queries):
    allocated_blocks = {}  # start -> size
    originally_occupied = set(i for i, val in enumerate(memory) if val == 1)
    current_memory = memory.copy()
    results = []
    
    for query in queries:
        if query[0] == "alloc":
            size = query[1]
            # Greedy: find leftmost free block
            start = find_leftmost_free_block(current_memory, size)
            if start != -1:
                for i in range(start, start + size):
                    current_memory[i] = 1
                allocated_blocks[start] = size
                results.append(start)
            else:
                results.append(-1)
                
        elif query[0] == "erase":
            index = query[1]
            if index in allocated_blocks:
                # Free allocated block
                block_size = allocated_blocks[index]
                for i in range(index, index + block_size):
                    current_memory[i] = 0
                del allocated_blocks[index]
                results.append(block_size)
            elif index in originally_occupied and current_memory[index] == 1:
                # Free originally occupied cell
                current_memory[index] = 0
                results.append(1)
            else:
                results.append(0)
    
    return results

def find_leftmost_free_block(memory, size):
    for i in range(len(memory) - size + 1):
        if all(memory[j] == 0 for j in range(i, i + size)):
            return i
    return -1
```

---

### 3. Array Query Processing

**Problem**: Process mixed update queries (add to array element) and count queries (count pairs where a[j] + b[j] = target).

**Pattern Recognition**: Query Processing with Updates

**Solution**:
```python
def solve_array_queries(a, b, queries):
    current_a = a.copy()
    results = []
    
    for query in queries:
        if query[0] == 0:  # Update: add x to a[i]
            i, x = query[1], query[2]
            if 0 <= i < len(current_a):
                current_a[i] += x
        else:  # Count: find pairs where a[j] + b[j] = target
            target = query[1]
            count = 0
            min_length = min(len(current_a), len(b))
            for j in range(min_length):
                if current_a[j] + b[j] == target:
                    count += 1
            results.append(count)
    
    return results
```

---

### 4. Rating System Problem

**Problem**: Process rating changes and classify final rating into levels (beginner/intermediate/advanced/pro).

**Pattern Recognition**: Sequential Processing + Classification

**Solution**:
```python
def user_rating_system(initial_rating, changes):
    current_rating = initial_rating
    
    # Apply all changes sequentially
    for change in changes:
        current_rating += change
    
    # Classify final rating
    if current_rating >= 2000:
        return "pro"
    elif current_rating >= 1500:
        return "advanced"
    elif current_rating >= 1000:
        return "intermediate"
    else:
        return "beginner"
```

---

## 📚 Study Plan (1 Week)

**Day 1-2**: Master templates + Easy problems
**Day 3-4**: Medium problems + pattern recognition practice
**Day 5-6**: Capital One specific patterns + hard problems
**Day 7**: Mock interviews + speed practice

**Daily Practice**: 2-3 problems, focus on quick pattern recognition and template application.

---

## 🎯 Key Success Tips for Capital One

1. **Pattern Recognition First**: Spend 30 seconds identifying the core pattern
2. **Template Selection**: Choose the right template quickly
3. **Clean Implementation**: Use the templates to write clean, readable code
4. **Edge Cases**: Always handle empty inputs, bounds checking
5. **Time Complexity**: Be aware of your solution's complexity
6. **Practice Speed**: Capital One values implementation speed

Remember: **Pattern → Template → Implementation** is your winning formula!