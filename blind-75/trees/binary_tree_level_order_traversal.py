'''
Binary Tree Level Order Traversal
Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Example 1:



Input: root = [1,2,3,4,5,6,7]

Output: [[1],[2,3],[4,5,6,7]]
Example 2:

Input: root = [1]

Output: [[1]]
Example 3:

Input: root = []

Output: []
Constraints:

0 <= The number of nodes in both trees <= 1000.
-1000 <= Node.val <= 1000

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the given tree.

Hint 1
The level of a tree refers to the nodes that are at equal distance from the root node. Can you think of an algorithm that traverses the tree level by level, rather than going deeper into the tree?

Hint 2
We can use the Breadth First Search (BFS) algorithm to traverse the tree level by level. BFS uses a queue data structure to achieve this. At each step of BFS, we only iterate over the queue up to its size at that step. Then, we take the left and right child pointers and add them to the queue. This allows us to explore all paths simultaneously.

Hint 3
The number of times we iterate the queue corresponds to the number of levels in the tree. At each step, we pop all nodes from the queue for the current level and add them collectively to the resultant array. This ensures that we capture all nodes at each level of the tree.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        