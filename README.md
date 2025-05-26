# blind-70-coding-interview-cheat-sheet
The Coding Patterns:

## 1. Two Pointers
### Explanation:
* Used for problems involving sorted arrays, linked lists, or needing to find pairs/triplets.
* When: Sorted arrays, pairs/triplets, palindrome checks
* Key: Use two indices moving inward/outward to reduce complexity

### Starter Code:
```
# Two pointers approach (often on sorted arrays or strings)
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
Used for substring or subarray problems involving contiguous elements.
When: Contiguous substring/subarray problems
Key: Expand/contract window to maintain constraints

### Starter Code:
```
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
Used to detect cycles or find middle elements.
When: Cycle detection, middle node in linked list
Key: Move pointers at different speeds to find meeting point

### Starter Code:
```
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
Used in problems involving trees, graphs, and permutations/combinations.
When: Trees, graphs, permutations, combinations
Key: Recursive exploration + backtrack to explore all paths
### Starter Code:
```
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
Used for shortest path in unweighted graphs or level order traversal in trees.
When: Shortest path, level traversal in trees/graphs
Key: Use queue for level-by-level traversal

### Starter Code:
```
from collections import deque

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

from collections import deque
def bfs(root):
    if not root: return []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        # process node
        for child in [node.left, node.right]:
            if child: queue.append(child)

```

### Problems List:
* Binary Tree Level Order Traversal
* Course Schedule
* Course Schedule II
* Word Ladder
* Minimum Depth of Binary Tree

## 6. Binary Search
### Explanation:
Used for searching in sorted arrays or applying to answer problems with monotonic properties.
When: Searching sorted arrays or monotonic functions
Key: Cut search space in half iteratively

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
Used for optimization problems with overlapping subproblems.
When: Overlapping subproblems, optimal substructure
Key: Store subproblem results to avoid re-computation

### Starter Code:
```
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
Used when a local optimal choice leads to a global optimal solution.
When: Locally optimal choices lead to global optimum
Key: Make best immediate choice, trust it leads to solution

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
Used in connectivity problems, detecting cycles in undirected graphs.
When: Connectivity, cycle detection in undirected graphs
Key: Track components, merge sets efficiently

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
Used in problems involving dependencies and ordering.
When: Ordering with dependencies (DAG)
Key: Remove nodes with zero in-degree iteratively

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
Used in problems requiring retrieval of min/max efficiently.
When: Efficient min/max retrieval
Key: Use heapq to maintain heap property

### Starter Code:
```
import heapq

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
Used in string search and prefix problems.
When: Prefix/search problems on strings
Key: Tree of dict nodes representing prefixes

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
Used in problems involving binary representations.
When: Problems on binary representations
Key: Use XOR, AND, OR, shifts for efficient ops

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
Including adjacency list/matrix and graph DFS/BFS.
When: Graph problems needing adjacency lists/matrices
Key: Use dict/list + BFS/DFS for traversal

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


Summary Table:
Pattern	Typical Problem Types
Two Pointers	Arrays, strings, pairs/triplets
Sliding Window	Substrings, subarrays, contiguous segments
Fast & Slow Pointers	Cycle detection, middle elements, linked lists
DFS / Backtracking	Trees, graphs, permutations, combinations
BFS	Shortest paths, level order traversal
Binary Search	Sorted arrays, monotonic functions
Dynamic Programming	Optimization, overlapping subproblems
Greedy	Local optimum problems
Union Find	Connectivity, cycles in graphs
Topological Sort	Dependency ordering
Heap / Priority Queue	Efficient min/max retrieval
Trie	Prefix and string search
Bit Manipulation	Binary operations, masks
Graph Representation	Graph traversal and construction

