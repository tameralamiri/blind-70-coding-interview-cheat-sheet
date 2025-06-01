## 🎯 Mock Interview Set 3: **Mixed Patterns & Advanced Logic**
*Focus: Combination of techniques, circular arrays, and complex simulations*

### **Question 1 (Easy-Medium - Circular Array Pattern)**
Given an array consisting of 1s and 0s and an integer `k`, find the number of **distinct** binary sequences of size `k` in the array. Treat the array as circular, meaning the last index of the array connects to the first index.

**Example 1**: `array = [1,0,1,0,1,1]`, `k = 3`
- Possible sequences: starting at index 0: `101`, starting at index 1: `010`, etc.
- Count distinct sequences: `{101, 010, 101, 011, 110, 100}` → result = 5

**Example 2**: `array = [1,0,1,0]`, `k = 2`  
- Possible sequences: `{10, 01, 10, 01}` → distinct: `{10, 01}` → result = 2

Your task is to return the count of distinct binary sequences.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(array.length²) will fit within the execution time limit.

---

### **Question 2 (Medium - Dynamic Scheduling)**
Imagine that you are managing a delivery system with drones. Each drone has a battery level (integer between 1 and 100) and can deliver packages. The delivery zones are classified based on distance:

- 1 <= distance < 20 = "local" (costs 5 battery)
- 20 <= distance < 50 = "regional" (costs 15 battery)  
- 50 <= distance < 80 = "long-distance" (costs 30 battery)
- 80 <= distance = "ultra-long" (costs 50 battery)

You are given an array `drones` with initial battery levels and an array `deliveries` containing delivery requests `[drone_id, distance]`. Process requests in order. If a drone doesn't have enough battery, skip that delivery. After each successful delivery, the drone's battery decreases by the cost amount.

Your task is to return an array indicating which deliveries were completed (true/false) and the final battery levels of all drones.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(deliveries.length²) will fit within the execution time limit.

---

### **Question 3 (Medium-Hard - Complex Resource Allocation)**
You are given three arrays: `servers`, `workloads`, and `priorities`. Each server has a capacity (integer), each workload has a size requirement (integer), and each priority indicates the order of processing (1 = highest priority).

The allocation rules are:
1. Process workloads in priority order (1, then 2, then 3, etc.)
2. For each workload, assign it to the server with the smallest available capacity that can fit it
3. If multiple servers have the same available capacity, choose the one with the lower index
4. If no server can fit the workload, skip it
5. Each server can handle multiple workloads as long as total doesn't exceed capacity

Your task is to return an array where `result[i]` contains the list of workload indices assigned to server `i`.

**Example**: `servers = [10, 5, 8]`, `workloads = [3, 7, 2, 4]`, `priorities = [2, 1, 3, 2]`

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(max(servers.length, workloads.length)³) will fit within the execution time limit.

---

### **Question 4 (Hard - Advanced Matrix Simulation)**
You are given a matrix `field` representing a farming simulation where each cell contains a crop type (integer) or is empty (0). You need to simulate seasonal changes over multiple cycles:

**Each cycle consists of:**
1. **Growth Phase**: Each crop spreads to adjacent empty cells (4-directional) if there are at least 2 crops of the same type adjacent to the empty cell
2. **Harvest Phase**: All crops of type `target_crop` are harvested (set to 0) 
3. **Replanting Phase**: New crops of type `new_crop` are planted in the top row if those cells are empty

You are given the initial `field`, number of `cycles`, `target_crop` type to harvest each cycle, and `new_crop` type to plant each cycle.

Your task is to return the final state of the field after all cycles.

**Example**: `field = [[1, 0, 1], [0, 1, 0], [0, 0, 0]]`, `cycles = 2`, `target_crop = 1`, `new_crop = 2`

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(field.length × field[0].length × cycles)² will fit within the execution time limit.

---
