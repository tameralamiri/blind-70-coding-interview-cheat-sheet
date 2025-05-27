# Blind75 - Coding Patterns:

## 1. Two Pointers
### Explanation:
When to use:
* The input is a sorted array or string
* You need to compare or sum pairs (e.g. find a target sum, reverse in place, check for palindrome)

Core logic:
* Use two pointers (left and right) starting from opposite ends or same point.
* Move the pointers inward or in different directions depending on conditions.



### Starter Code:
```
# Two pointers approach (often on sorted arrays or strings)
def default_two_pointers(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        # logic
        left += 1
        right -= 1

def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]
```

### Problems List:
* Valid Palindrome
* Two Sum II - Input Array Is Sorted
* Container With Most Water
* 3Sum
* Sort Colors
* Squares of a Sorted Array
* Remove Duplicates from Sorted Array

## 2. Sliding Window
### Explanation:
When to use:
* You’re working with contiguous subarrays or substrings
* You need to optimize something (e.g., max sum, longest/shortest substring, etc.)

Core logic:
* Keep a window of elements using two pointers (start, end).
* Slide the window while maintaining the problem constraint (e.g., unique characters, target sum).
* Shrink or expand based on conditions.

### Starter Code:
```
def default_sliding_window(s):
    window = set()
    left = 0
    for right in range(len(s)):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])

# Sliding window example: Longest substring without repeating characters
def length_of_longest_substring(s):
    seen, left, max_len = set(), 0, 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right-left+1)
    return max_len
```

### Problems List:
* Minimum Window Substring
* Longest Substring Without Repeating Characters
* Permutation in String
* Sliding Window Maximum
* Find All Anagrams in a String

## 3. Fast and Slow Pointers (Floyd’s Cycle Detection)
### Explanation:
When to use:
* Linked list problems (e.g. detecting cycles, finding middle node)
* Array cycle problems (e.g. Happy Number)

Core logic:
* Use two pointers: slow (1 step), fast (2 steps).
* If there’s a cycle, fast will meet slow.
* Use it when you want to detect loops or distances efficiently.

### Starter Code:
```
def default_fast_slow(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

# Detect cycle in linked list using fast and slow pointers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

### Problems List:
* Linked List Cycle
* Happy Number
* Middle of the Linked List
* Reverse Linked List
* Intersection of Two Linked Lists

## 4. Depth-First Search (DFS) / Backtracking
### Explanation:
When to use:
* Recursive problems, especially:
    * Graphs or Trees traversal
    * Generate all combinations, subsets, permutations
    * Constraint satisfaction (sudoku, word search)

Core logic:
* Explore all possible decisions (recursive tree).
* If a path doesn’t work, backtrack and try another.
* Use recursion, often with a helper function and state tracking (e.g. path, index).

### Starter Code:
```
def dfs(node, path):
    if some_condition:
        result.append(path[:])
        return
    for option in options:
        path.append(option)
        dfs(node, path)
        path.pop()

# DFS example: Number of Islands (grid DFS)
def dfs(grid, r, c):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
        return
    grid[r][c] = '0'  # mark visited
    dfs(grid, r + 1, c)
    dfs(grid, r - 1, c)
    dfs(grid, r, c + 1)
    dfs(grid, r, c - 1)

def num_islands(grid):
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                dfs(grid, r, c)
                count += 1
    return count
```

### Problems List:
* Number of Islands
* Clone Graph
* Word Search
* Subsets
* Permutations
* Combination Sum
* Letter Case Permutation
* Generate Parentheses

## 5. Breadth-First Search (BFS)
### Explanation:
When to use:
* Find the shortest path in unweighted graphs
* Level-by-level traversal (e.g. trees, graphs)
* Problems with "minimum steps" or spreading processes

Core logic:
* Use a queue to visit nodes in order of distance.
* Track visited nodes to avoid loops.
* Expand from source to all neighbors at each level.

### Starter Code:
```
from collections import deque

def bfs(root):
    if not root: return []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        # process node
        for child in [node.left, node.right]:
            if child: queue.append(child)

# BFS example: Level order traversal of binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []
    res = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res
```

### Problems List:
* Binary Tree Level Order Traversal
* Course Schedule
* Course Schedule II
* Word Ladder
* Minimum Depth of Binary Tree

## 6. Binary Search
### Explanation:
When to use:
* Array is sorted or the problem has a monotonic property (function increasing or decreasing)
* You’re searching for a value, count, or index

Core logic:
* Divide the array in half each time.
* Narrow your search space with mid = (low + high) // 2.
* Adjust boundaries (left and right) based on conditions.

### Starter Code:
```
# Binary search in a sorted array
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Problems List:
* Search in Rotated Sorted Array
* Find Minimum in Rotated Sorted Array
* Kth Largest Element in an Array
* Median of Two Sorted Arrays
* Search Insert Position
* Guess Number Higher or Lower

## 7. Dynamic Programming (DP)
### Explanation:
When to use:
* The problem has overlapping subproblems and optimal substructure
* You're asked for min/max/ways/count of something

Core logic:
* Break down the problem into smaller subproblems
* Store results in a table (bottom-up) or cache (top-down with memoization)
* Use previous results to build the final answer

### Starter Code:
```
@lru_cache(None)
def dp(i):
    if i == 0: return 0
    return min(dp(i-1), dp(i-2)) + cost[i]

# DP example: Climbing Stairs
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

### Problems List:
* Climbing Stairs
* House Robber
* Coin Change
* Longest Increasing Subsequence
* Word Break
* Maximum Subarray
* Unique Paths
* Decode Ways

## 8. Greedy
### Explanation:
When to use:
* You can make a local optimal choice at each step that leads to a global solution
* Often used in:
    * Interval problems (merge, select)
    * Resource allocation (jump game, gas station)

Core logic:
* Pick the best option available now
* Don’t revisit previous choices
* No backtracking

### Starter Code:
```
# Greedy example: Jump Game
def can_jump(nums):
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    return True
```

### Problems List:
* Jump Game
* Gas Station
* Assign Cookies
* Queue Reconstruction by Height

## 9. Union Find / Disjoint Set
### Explanation:
When to use:
* You need to track connected components
* Check if adding an edge creates a cycle
* Problems like:
    * Graph Valid Tree
    * Number of Connected Components

Core logic:
* Each node has a parent; use path compression & union by rank for efficiency
* Check if two nodes are in the same set or not

### Starter Code:
```
# Union Find implementation
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
        return x

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True
```

### Problems List:
* Number of Connected Components in an Undirected Graph
* Redundant Connection
* Graph Valid Tree


## 10. Topological Sort
### Explanation:
When to use:
* You have dependencies between tasks (e.g. course scheduling)
* Directed Acyclic Graph (DAG)

Core logic:
* Count incoming edges (in-degree)
* Start with nodes having 0 in-degree
* Remove edges as you process, keeping track of ordering

### Starter Code:
```
from collections import deque, defaultdict

def topological_sort(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1

    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) == numCourses:
        return topo_order
    else:
        return []  # cycle detected
```

### Problems List:
* Course Schedule
* Course Schedule II

## 11. Heap / Priority Queue
### Explanation:
When to use:
* You need to frequently access the min/max element
* Scenarios:
    * Get top K elements
    * Merge sorted lists
    * Scheduling problems

Core logic:
* Use a heap (heapq) to maintain order of elements efficiently
* heapq is a min-heap by default (use -val for max heap)

### Starter Code:
```
import heapq
heapq.heapify(nums)
heapq.heappush(nums, val)
heapq.heappop(nums)
heapq.nlargest(k, nums)


# Find k largest elements
def k_largest(nums, k):
    return heapq.nlargest(k, nums)

# Or heapify and pop k times:
def k_largest_heap(nums, k):
    heapq.heapify(nums)
    result = []
    for _ in range(len(nums) - k):
        heapq.heappop(nums)
    return nums  # now the heap contains the k largest
```

### Problems List:
* Kth Largest Element in an Array
* Merge K Sorted Lists
* Top K Frequent Elements

## 12. Trie (Prefix Tree)
### Explanation:
When to use:
* You deal with prefixes or dictionary-based string matching
* Autocomplete, word search, spell-check

Core logic:
* Tree of characters where each path from root to leaf is a word
* Allows fast prefix checks and insertions

### Starter Code:
```
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word
```

### Problems List:
* Implement Trie
* Word Search II

## 13. Bit Manipulation
### Explanation:
When to use:
* Problem involves binary representation or performance-sensitive operations
* E.g.:
    * Single Number
    * Counting bits
    * Subset generation

Core logic:
* Use &, |, ^, <<, >>
* Bitwise tricks to toggle/check/set/clear bits
* XOR is great for cancelling out pairs

### Starter Code:
```
# Example: Single Number (XOR all numbers)
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

### Problems List:
* Single Number
* Number of 1 Bits
* Missing Number

## 14. Graph Representation & Traversal
### Explanation:
When to use:
* You’re working with networks, connections, dependencies
* Problem is naturally a graph (even if not explicitly given)

Core logic:
* Use adjacency list or adjacency matrix
* Apply DFS or BFS to traverse or search

### Starter Code:
```
from collections import defaultdict, deque

def build_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # if undirected
    return graph

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### Problems List:
* Clone Graph
* Number of Islands
* Graph Valid Tree


## Summary Table:


| Pattern              | Typical Problem Types                                | Common Clues in Problem                      |
|----------------------|------------------------------------------------------| -------------------------------------------- |
| Two Pointers         | Arrays, strings, pairs/triplets                      | "sorted", "pairs", "palindrome"              |
| Sliding Window       | Substrings, subarrays, contiguous segments           | "longest/shortest subarray/substring"        |
| Fast & Slow Pointers | Cycle detection, middle elements, linked lists       | "cycle", "linked list", "loop"               |
| DFS / Backtracking   | Trees, graphs, permutations, combinations            | "all combinations", "paths", "choices"       |
| BFS                  | Shortest paths, level order traversal                | "shortest path", "minimum steps"             |
| Binary Search        | Sorted arrays, monotonic functions                   | "sorted", "monotonic", "find target"         |
| Dynamic Programming  | Optimization, overlapping subproblems                | "ways", "min/max", "overlapping subproblems" |
| Greedy               | Local optimum problems                               | "best now", "maximize/minimize", "no redo"   |
| Union Find           | Connectivity, cycles in graphs                       | "connected components", "cycle", "disjoint"  |
| Topological Sort     | Dependency ordering                                  | "order tasks", "prerequisites", "DAG"        |
| Heap / Priority Queue| Efficient min/max retrieval                          | "top k", "closest", "min/max efficiently"    |
| Trie                 | Prefix and string search                             | "prefix", "dictionary", "autocomplete"       |
| Bit Manipulation     | Binary operations, masks                             | "binary", "odd one out", "XOR trick"         |
| Graph Representation | Graph traversal and construction                     | "network", "reachability", "paths"           |


