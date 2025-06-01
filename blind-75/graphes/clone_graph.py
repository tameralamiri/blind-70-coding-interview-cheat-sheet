'''
Clone Graph
Given a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains an integer value and a list of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.

Example 1:



Input: adjList = [[2],[1,3],[2]]

Output: [[2],[1,3],[2]]
Explanation: There are 3 nodes in the graph.
Node 1: val = 1 and neighbors = [2].
Node 2: val = 2 and neighbors = [1, 3].
Node 3: val = 3 and neighbors = [2].

Example 2:



Input: adjList = [[]]

Output: [[]]
Explanation: The graph has one node with no neighbors.

Example 3:

Input: adjList = []

Output: []
Explanation: The graph is empty.

Constraints:

0 <= The number of nodes in the graph <= 100.
1 <= Node.val <= 100
There are no duplicate edges and no self-loops in the graph.


Recommended Time & Space Complexity
You should aim for a solution with O(V + E) time and O(E) space, where V is the number of vertices and E is the number of edges in the given graph.

Hint 1
We are given only the reference to the node in the graph. Cloning the entire graph means we need to clone all the nodes as well as their child nodes. We can't just clone the node and its neighbor and return the node. We also need to clone the entire graph. Can you think of a recursive way to do this, as we are cloning nodes in a nested manner? Also, can you think of a data structure that can store the nodes with their cloned references?

Hint 2
We can use the Depth First Search (DFS) algorithm. We use a hash map to map the nodes to their cloned nodes. We start from the given node. At each step of the DFS, we create a node with the current node's value. We then recursively go to the current node's neighbors and try to clone them first. After that, we add their cloned node references to the current node's neighbors list. Can you think of a base condition to stop this recursive path?

Hint 3
We stop this recursive path when we encounter a node that has already been cloned or visited. This DFS approach creates an exact clone of the given graph, and we return the clone of the given node.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        