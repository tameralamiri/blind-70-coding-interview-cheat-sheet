'''
Binary Tree Maximum Path Sum
Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

Example 1:



Input: root = [1,2,3]

Output: 6
Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.

Example 2:



Input: root = [-15,10,20,null,null,15,5,-5]

Output: 40
Explanation: The path is 15 -> 20 -> 5 with a sum of 15 + 20 + 5 = 40.

Constraints:

1 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000


Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the given tree.

Hint 1
A brute force solution would involve checking the path sum between every pair of nodes in the tree, leading to an O(n^2) time complexity. Can you think of a more efficient approach? Consider what information you would need at each node to calculate the path sum if it passes through the current node.

Hint 2
At a node, there are three scenarios to compute the maximum path sum that includes the current node. One includes both the left and right subtrees, with the current node as the connecting node. Another path sum includes only one of the subtrees (either left or right), but not both. Another considers the path sum extending from the current node to the parent. However, the parent’s contribution is computed during the traversal at the parent node. Can you implement this?

Hint 3
We can use the Depth First Search (DFS) algorithm to traverse the tree. We maintain a global variable to track the maximum path sum. At each node, we first calculate the maximum path sum from the left and right subtrees by traversing them. After that, we compute the maximum path sum at the current node. This approach follows a post-order traversal, where we visit the subtrees before processing the current node.

Hint 4
We return the maximum path sum from the current node to its parent, considering only one of the subtrees (either left or right) to extend the path. While calculating the left and right subtree path sums, we also ensure that we take the maximum with 0 to avoid negative sums, indicating that we should not include the subtree path in the calculation of the maximum path at the current node.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        