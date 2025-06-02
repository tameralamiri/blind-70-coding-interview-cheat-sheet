## 🎯 Mock Interview Set 1: **Greedy & Resource Management**
*Focus: Resource allocation, optimization, and constraint handling*

### **Question 1 (Easy - Rating System Variant)**
Imagine that you are managing user subscription levels for a streaming platform. Each user has a current subscription tier (an integer between 1 and 100), and a corresponding access level. The subscription tiers are based on the following rules:

- 1 <= tier < 25 = "basic"
- 25 <= tier < 50 = "standard" 
- 50 <= tier < 75 = "premium"
- 75 <= tier = "platinum"

You are given an initial tier value and an array of integers `adjustments` representing changes to the tier due to promotions or downgrades. Your task is to calculate the final tier and return the access level corresponding to that tier.

It is guaranteed that changes to the tier value will never result in it becoming less than 1 or greater than 100.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(adjustments.length²) will fit within the execution time limit.

```python
# Test Case 1: Basic tier
initial_tier = 10
adjustments = [5, -2, 3]
# Expected: final_tier = 16, access_level = "basic"

# Test Case 2: Crosses multiple tiers
initial_tier = 20
adjustments = [10, 15, 5]
# Expected: final_tier = 50, access_level = "premium"

# Test Case 3: Platinum tier
initial_tier = 80
adjustments = [-5, 10, -3]
# Expected: final_tier = 82, access_level = "platinum"

# Test Case 4: Boundary values
initial_tier = 24
adjustments = [1]
# Expected: final_tier = 25, access_level = "standard"

# Test Case 5: Edge case - stays at boundary
initial_tier = 75
adjustments = [0, -1, 1]
# Expected: final_tier = 75, access_level = "platinum"
```

---

### **Question 2 (Easy-Medium - Query Processing)**
You are given two arrays of integers `scores` and `bonuses` and an array `operations` containing the operations you are required to process. Every `operations[i]` can have one of the following two forms:

- `[0, i, x]`: In this case, you need to add `x` to the current value of `scores[i]`.
- `[1, target]`: In this case, you need to find the total number of pairs of indices `j` such that `scores[j] + bonuses[j] = target`.

Perform the given operations in order and return an array containing the results of the operations of type `[1, target]`.

**Example**: For `scores = [2, 4, 6]`, `bonuses = [3, 1]`, and `operations = [[1, 7], [0, 1, 2], [1, 7]]`, the output should be `solution(scores, bonuses, operations)`.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(max(scores.length, bonuses.length)³) will fit within the execution time limit.

```python
# Test Case 1: Basic example
scores = [2, 4, 6]
bonuses = [3, 1, 2]
operations = [[1, 7], [0, 1, 2], [1, 7], [1, 9]]

# Test Case 2: No matches
scores = [1, 2, 3]
bonuses = [1, 1, 1]
operations = [[1, 10], [0, 0, 5], [1, 10]]

# Test Case 3: Multiple matches
scores = [5, 5, 5]
bonuses = [2, 2, 2]
operations = [[1, 7], [0, 0, 1], [1, 7], [1, 8]]
```
---

### **Question 3 (Medium - Resource Matching)**
Imagine that you are organizing team assignments for a software project. Each developer has a skill level (integer), and each task has a required difficulty level (integer). A developer can only be assigned to a task if their skill level is **greater than or equal to** the task difficulty. However, each developer can only work on a maximum of 2 tasks before becoming unavailable for additional assignments.

Given two arrays `developers` and `tasks`, where `developers[i]` corresponds to the skill level of the ith developer, and `tasks[j]` corresponds to the difficulty of the jth task, your task is to return the maximum number of tasks you can complete.

To compute the answer, you need to assign each developer optimally, going from the most skilled developer to the least skilled developer. Use each developer to complete the most difficult tasks they can handle and move to the next developer if the current developer was assigned 2 tasks or if they cannot handle any remaining tasks.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(max(developers.length, tasks.length)³) will fit within the execution time limit.

```python
# Test Case 1: Basic assignment
developers = [3, 2, 1, 4]
tasks = [1, 2, 3, 2]
# Expected: 4 (all tasks can be completed)

# Test Case 2: More tasks than capacity
developers = [5, 3]
tasks = [1, 2, 3, 4, 5]
# Expected: 4 (each developer takes 2 tasks max)

# Test Case 3: Some developers can't handle tasks
developers = [1, 2]
tasks = [3, 4, 5]
# Expected: 0 (no developer can handle any task)

# Test Case 4: Optimal assignment needed
developers = [4, 3, 2]
tasks = [4, 3, 2, 1, 1]
# Expected: 5 (strategic assignment required)
```
---

### **Question 4 (Medium-Hard - Advanced Resource Management)**
You are given an array of integers `storage` consisting of 0s and 1s—where the corresponding storage unit is available or not. `storage[i] = 0` means that the ith storage unit is available, and `storage[i] = 1` means it's occupied.

Your task is to perform two types of operations:

- `reserve x`: Find the right-most storage block of `x` consecutive available storage units and mark these units as occupied (i.e., find the right-most contiguous subarray of 0s, and replace them all with 1s). If there are no blocks with `x` consecutive available units, return -1; otherwise return the index of the first position of the reserved block segment.
- `release index`: If there exists a reserved storage block starting at position `index`, free all its storage units. Otherwise, if the storage cell at position `index` was occupied before the very first operation ever applied to the storage, free this cell only. Return the length of the released storage block. If there is no reserved block starting at the position `index`, return 0.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(storage.length³) will fit within the execution time limit.

```python
# Test Case 1: Basic operations
storage = [0, 0, 1, 0, 0, 0, 1]
operations = [
    ("reserve", 2),    # Should return 3 (rightmost block of 2 zeros)
    ("reserve", 1),    # Should return 0 or 1 
    ("release", 3),    # Release the block starting at index 3
    ("reserve", 3)     # Should return 3 again
]

# Test Case 2: No available blocks
storage = [1, 1, 1, 0, 1]
operations = [
    ("reserve", 2),    # Should return -1 (no block of size 2)
    ("reserve", 1),    # Should return 3
    ("release", 3)     # Should return 1
]

# Test Case 3: Complex sequence
storage = [0, 0, 0, 0, 1, 0, 0]
operations = [
    ("reserve", 3),    # Should find rightmost block of 3
    ("reserve", 2),    # Should find remaining block
    ("release", 0),    # Release if exists
    ("reserve", 4)     # Should return -1 or find new block
]
```
---


