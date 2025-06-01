# Capital One Mock Interview Set 3: Mixed Patterns & Advanced Logic

*Focus: Combination of techniques, circular arrays, and complex simulations*

## ⏱️ Time Allocation: 45 minutes total
- **Question 1**: 8 minutes (Easy-Medium)
- **Question 2**: 10 minutes (Medium) 
- **Question 3**: 12 minutes (Medium-Hard)
- **Question 4**: 15 minutes (Hard)

---

## Question 1 (Easy-Medium - Circular Array Pattern)

Given an array consisting of 1s and 0s and an integer `k`, find the number of **distinct** binary sequences of size `k` in the array. Treat the array as circular, meaning the last index of the array connects to the first index.

**Example 1**: `array = [1,0,1,0,1,1]`, `k = 3`
- Possible sequences: starting at index 0: `101`, starting at index 1: `010`, etc.
- Count distinct sequences: `{101, 010, 101, 011, 110, 100}` → result = 5

**Example 2**: `array = [1,0,1,0]`, `k = 2`  
- Possible sequences: `{10, 01, 10, 01}` → distinct: `{10, 01}` → result = 2

Your task is to return the count of distinct binary sequences.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(array.length²) will fit within the execution time limit.

### Pattern Recognition
- **Type**: Circular Array Processing with Pattern Collection
- **Template**: Set-based deduplication with modular arithmetic

### Solution Approach
```python
def count_distinct_sequences(array, k):
    if not array or k <= 0 or k > len(array):
        return 0
    
    n = len(array)
    sequences = set()
    
    # Generate all possible sequences of length k
    for start in range(n):
        sequence = []
        for i in range(k):
            # Use modular arithmetic for circular indexing
            idx = (start + i) % n
            sequence.append(str(array[idx]))
        
        # Convert to string and add to set
        seq_str = ''.join(sequence)
        sequences.add(seq_str)
    
    return len(sequences)
```

---

## Question 2 (Medium - Dynamic Scheduling)

Imagine that you are managing a delivery system with drones. Each drone has a battery level (integer between 1 and 100) and can deliver packages. The delivery zones are classified based on distance:

- 1 <= distance < 20 = "local" (costs 5 battery)
- 20 <= distance < 50 = "regional" (costs 15 battery)  
- 50 <= distance < 80 = "long-distance" (costs 30 battery)
- 80 <= distance = "ultra-long" (costs 50 battery)

You are given an array `drones` with initial battery levels and an array `deliveries` containing delivery requests `[drone_id, distance]`. Process requests in order. If a drone doesn't have enough battery, skip that delivery. After each successful delivery, the drone's battery decreases by the cost amount.

Your task is to return an array indicating which deliveries were completed (true/false) and the final battery levels of all drones.

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(deliveries.length²) will fit within the execution time limit.

### Pattern Recognition
- **Type**: Resource Management with Classification
- **Template**: State tracking with cost calculation

### Solution Approach
```python
def drone_delivery_system(drones, deliveries):
    battery_levels = drones.copy()
    delivery_results = []
    
    def get_battery_cost(distance):
        if distance < 20:
            return 5  # local
        elif distance < 50:
            return 15  # regional
        elif distance < 80:
            return 30  # long-distance
        else:
            return 50  # ultra-long
    
    for drone_id, distance in deliveries:
        if 0 <= drone_id < len(battery_levels):
            cost = get_battery_cost(distance)
            
            if battery_levels[drone_id] >= cost:
                # Delivery successful
                battery_levels[drone_id] -= cost
                delivery_results.append(True)
            else:
                # Not enough battery
                delivery_results.append(False)
        else:
            # Invalid drone ID
            delivery_results.append(False)
    
    return {
        'completed_deliveries': delivery_results,
        'final_battery_levels': battery_levels
    }
```

---

## Question 3 (Medium-Hard - Complex Resource Allocation)

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

### Pattern Recognition
- **Type**: Greedy Resource Allocation with Priority Sorting
- **Template**: Multi-constraint optimization with best-fit algorithm

### Solution Approach
```python
def allocate_workloads(servers, workloads, priorities):
    n_servers = len(servers)
    n_workloads = len(workloads)
    
    # Initialize result and server usage tracking
    result = [[] for _ in range(n_servers)]
    server_used = [0] * n_servers  # Track used capacity per server
    
    # Create workload list with indices and sort by priority
    workload_data = []
    for i in range(n_workloads):
        workload_data.append((priorities[i], workloads[i], i))
    
    # Sort by priority (1 = highest priority comes first)
    workload_data.sort(key=lambda x: x[0])
    
    # Process each workload in priority order
    for priority, size, workload_idx in workload_data:
        best_server = -1
        best_available_capacity = float('inf')
        
        # Find best server (smallest available capacity that can fit)
        for server_idx in range(n_servers):
            available_capacity = servers[server_idx] - server_used[server_idx]
            
            # Check if server can fit this workload
            if available_capacity >= size:
                # Choose server with smallest available capacity
                # If tie, choose lower index (already handled by iteration order)
                if available_capacity < best_available_capacity:
                    best_available_capacity = available_capacity
                    best_server = server_idx
        
        # Assign workload to best server if found
        if best_server != -1:
            result[best_server].append(workload_idx)
            server_used[best_server] += size
    
    return result
```

---

## Question 4 (Hard - Advanced Matrix Simulation)

You are given a matrix `field` representing a farming simulation where each cell contains a crop type (integer) or is empty (0). You need to simulate seasonal changes over multiple cycles:

**Each cycle consists of:**
1. **Growth Phase**: Each crop spreads to adjacent empty cells (4-directional) if there are at least 2 crops of the same type adjacent to the empty cell
2. **Harvest Phase**: All crops of type `target_crop` are harvested (set to 0) 
3. **Replanting Phase**: New crops of type `new_crop` are planted in the top row if those cells are empty

You are given the initial `field`, number of `cycles`, `target_crop` type to harvest each cycle, and `new_crop` type to plant each cycle.

Your task is to return the final state of the field after all cycles.

**Example**: `field = [[1, 0, 1], [0, 1, 0], [0, 0, 0]]`, `cycles = 2`, `target_crop = 1`, `new_crop = 2`

**Note**: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(field.length × field[0].length × cycles)² will fit within the execution time limit.

### Pattern Recognition
- **Type**: Complex Matrix Simulation with Multi-Phase Processing
- **Template**: State-based simulation with neighbor counting

### Solution Approach
```python
def farming_simulation(field, cycles, target_crop, new_crop):
    if not field or not field[0]:
        return field
    
    rows, cols = len(field), len(field[0])
    current_field = [row[:] for row in field]  # Deep copy
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 4-directional
    
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    def growth_phase():
        # Find cells that should grow new crops
        new_crops = []
        
        for r in range(rows):
            for c in range(cols):
                if current_field[r][c] == 0:  # Empty cell
                    # Count neighbors by crop type
                    neighbor_counts = {}
                    
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if is_valid(nr, nc) and current_field[nr][nc] != 0:
                            crop_type = current_field[nr][nc]
                            neighbor_counts[crop_type] = neighbor_counts.get(crop_type, 0) + 1
                    
                    # Check if any crop type has at least 2 neighbors
                    for crop_type, count in neighbor_counts.items():
                        if count >= 2:
                            new_crops.append((r, c, crop_type))
                            break  # Only one crop type can grow per cell
        
        # Apply growth
        for r, c, crop_type in new_crops:
            current_field[r][c] = crop_type
    
    def harvest_phase():
        # Remove all crops of target_crop type
        for r in range(rows):
            for c in range(cols):
                if current_field[r][c] == target_crop:
                    current_field[r][c] = 0
    
    def replanting_phase():
        # Plant new_crop in empty cells of top row
        for c in range(cols):
            if current_field[0][c] == 0:
                current_field[0][c] = new_crop
    
    # Execute cycles
    for cycle in range(cycles):
        growth_phase()
        harvest_phase()
        replanting_phase()
    
    return current_field
```

---

## 🎯 Key Takeaways for Set 3

1. **Circular Array Handling**: Use modular arithmetic for wraparound indexing
2. **Multi-Phase Simulations**: Break complex processes into discrete steps
3. **Priority-Based Processing**: Sort data structures by priority before processing
4. **Resource Constraints**: Track multiple constraint types simultaneously
5. **State Evolution**: Maintain and update complex state across iterations
6. **Neighbor Analysis**: Count and classify neighboring elements effectively
7. **Best-Fit Algorithms**: Find optimal assignments under multiple criteria