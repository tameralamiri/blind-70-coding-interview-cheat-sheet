# Capital One Mock Interview Set 1: Greedy & Resource Management

*Focus: Resource allocation, optimization, and constraint handling*

## ⏱️ Time Allocation: 45 minutes total
- **Question 1**: 8 minutes (Easy)
- **Question 2**: 10 minutes (Easy-Medium) 
- **Question 3**: 12 minutes (Medium)
- **Question 4**: 15 minutes (Medium-Hard)

---

## Question 1 (Easy - Rating System Variant)

Imagine that you are managing user subscription levels for a streaming platform. Each user has a current subscription tier (an integer between 1 and 100), and a corresponding access level. The subscription tiers are based on the following rules:

- 1 <= tier < 25 = "basic"
- 25 <= tier < 50 = "standard" 
- 50 <= tier < 75 = "premium"
- 75 <= tier = "platinum"

You are given an initial tier value and an array of integers `adjustments` representing changes to the tier due to promotions or downgrades. Your task is to calculate the final tier and return the access level corresponding to that tier.

It is guaranteed that changes to the tier value will never result in it becoming less than 1 or greater than 100.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(adjustments.length²) will fit within the execution time limit.

### Pattern Recognition
- **Type**: Sequential Processing + Classification
- **Template**: Rating/Level Systems (Template 4)

### Solution Approach
```python
def subscription_tier_system(initial_tier, adjustments):
    current_tier = initial_tier
    
    # Apply all adjustments sequentially
    for adjustment in adjustments:
        current_tier += adjustment
    
    # Classify final tier
    if current_tier >= 75:
        return "platinum"
    elif current_tier >= 50:
        return "premium"
    elif current_tier >= 25:
        return "standard"
    else:
        return "basic"
```

---

## Question 2 (Easy-Medium - Query Processing)

You are given two arrays of integers `scores` and `bonuses` and an array `operations` containing the operations you are required to process. Every `operations[i]` can have one of the following two forms:

- `[0, i, x]`: In this case, you need to add `x` to the current value of `scores[i]`.
- `[1, target]`: In this case, you need to find the total number of pairs of indices `j` such that `scores[j] + bonuses[j] = target`.

Perform the given operations in order and return an array containing the results of the operations of type `[1, target]`.

**Example**: For `scores = [2, 4, 6]`, `bonuses = [3, 1]`, and `operations = [[1, 7], [0, 1, 2], [1, 7]]`, the output should be `solution(scores, bonuses, operations)`.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(max(scores.length, bonuses.length)³) will fit within the execution time limit.

### Pattern Recognition
- **Type**: Query Processing with Updates
- **Template**: Query Processing (Template 2)

### Solution Approach
```python
def solve_score_queries(scores, bonuses, operations):
    current_scores = scores.copy()
    results = []
    
    for operation in operations:
        if operation[0] == 0:  # Update operation
            i, x = operation[1], operation[2]
            if 0 <= i < len(current_scores):
                current_scores[i] += x
        else:  # Count operation
            target = operation[1]
            count = 0
            min_length = min(len(current_scores), len(bonuses))
            for j in range(min_length):
                if current_scores[j] + bonuses[j] == target:
                    count += 1
            results.append(count)
    
    return results
```

---

## Question 3 (Medium - Resource Matching)

Imagine that you are organizing team assignments for a software project. Each developer has a skill level (integer), and each task has a required difficulty level (integer). A developer can only be assigned to a task if their skill level is **greater than or equal to** the task difficulty. However, each developer can only work on a maximum of 2 tasks before becoming unavailable for additional assignments.

Given two arrays `developers` and `tasks`, where `developers[i]` corresponds to the skill level of the ith developer, and `tasks[j]` corresponds to the difficulty of the jth task, your task is to return the maximum number of tasks you can complete.

To compute the answer, you need to assign each developer optimally, going from the most skilled developer to the least skilled developer. Use each developer to complete the most difficult tasks they can handle and move to the next developer if the current developer was assigned 2 tasks or if they cannot handle any remaining tasks.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(max(developers.length, tasks.length)³) will fit within the execution time limit.

### Pattern Recognition
- **Type**: Greedy Resource Matching with Constraints
- **Template**: Resource Matching (Template 1)

### Solution Approach
```python
def assign_developers_to_tasks(developers, tasks):
    if not developers or not tasks:
        return 0
    
    # Sort developers by skill (highest first) and tasks by difficulty (highest first)
    developers.sort(reverse=True)
    available_tasks = sorted(tasks, reverse=True)
    
    completed_tasks = 0
    
    for developer_skill in developers:
        tasks_assigned = 0  # Each developer can handle max 2 tasks
        
        while tasks_assigned < 2 and available_tasks:
            # Find most difficult task this developer can handle
            task_idx = -1
            
            for i, task_difficulty in enumerate(available_tasks):
                if developer_skill >= task_difficulty:
                    task_idx = i
                    break
            
            if task_idx != -1:
                available_tasks.pop(task_idx)
                completed_tasks += 1
                tasks_assigned += 1
            else:
                break  # Developer can't handle any remaining tasks
    
    return completed_tasks
```

---

## Question 4 (Medium-Hard - Advanced Resource Management)

You are given an array of integers `storage` consisting of 0s and 1s—where the corresponding storage unit is available or not. `storage[i] = 0` means that the ith storage unit is available, and `storage[i] = 1` means it's occupied.

Your task is to perform two types of operations:

- `reserve x`: Find the right-most storage block of `x` consecutive available storage units and mark these units as occupied (i.e., find the right-most contiguous subarray of 0s, and replace them all with 1s). If there are no blocks with `x` consecutive available units, return -1; otherwise return the index of the first position of the reserved block segment.
- `release index`: If there exists a reserved storage block starting at position `index`, free all its storage units. Otherwise, if the storage cell at position `index` was occupied before the very first operation ever applied to the storage, free this cell only. Return the length of the released storage block. If there is no reserved block starting at the position `index`, return 0.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(storage.length³) will fit within the execution time limit.

### Pattern Recognition
- **Type**: Interval Allocation with Right-most Search
- **Template**: Modified Interval/Memory Allocation (Template 3)

### Solution Approach
```python
def solve_storage_queries(storage, queries):
    reserved_blocks = {}  # start -> size
    originally_occupied = set(i for i, val in enumerate(storage) if val == 1)
    current_storage = storage.copy()
    results = []
    
    for query in queries:
        if query[0] == "reserve":
            size = query[1]
            # Find rightmost free block
            start = find_rightmost_free_block(current_storage, size)
            if start != -1:
                for i in range(start, start + size):
                    current_storage[i] = 1
                reserved_blocks[start] = size
                results.append(start)
            else:
                results.append(-1)
                
        elif query[0] == "release":
            index = query[1]
            if index in reserved_blocks:
                # Free reserved block
                block_size = reserved_blocks[index]
                for i in range(index, index + block_size):
                    current_storage[i] = 0
                del reserved_blocks[index]
                results.append(block_size)
            elif index in originally_occupied and current_storage[index] == 1:
                # Free originally occupied cell
                current_storage[index] = 0
                results.append(1)
            else:
                results.append(0)
    
    return results

def find_rightmost_free_block(storage, size):
    # Scan from right to left
    for i in range(len(storage) - size, -1, -1):
        if all(storage[j] == 0 for j in range(i, i + size)):
            return i
    return -1
```

---

## 🎯 Key Takeaways for Set 1

1. **Greedy Strategy**: Always make locally optimal choices
2. **Resource Constraints**: Track usage limits and availability
3. **Query Processing**: Handle mixed operations efficiently
4. **State Management**: Maintain current state throughout operations
5. **Edge Cases**: Empty inputs, bounds checking, invalid operations

