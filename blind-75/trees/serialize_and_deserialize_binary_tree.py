'''
Serialize and Deserialize Binary Tree
Implement an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across a network to be reconstructed later in another computer environment.

You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. There is no additional restriction on how your serialization/deserialization algorithm should work.

Note: The input/output format in the examples is the same as how NeetCode serializes a binary tree. You do not necessarily need to follow this format.

Example 1:



Input: root = [1,2,3,null,null,4,5]

Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []

Output: []
Constraints:

0 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the given tree.

Hint 1
A straightforward way to serialize a tree is by traversing it and adding nodes to a string separated by a delimiter (example: ","), but this does not handle null nodes effectively. During deserialization, it becomes unclear where to stop or how to handle missing children. Can you think of a way to indicate null nodes explicitly?

Hint 2
Including a placeholder for null nodes (example: "N") during serialization ensures that the exact structure of the tree is preserved. This placeholder allows us to identify missing children and reconstruct the tree accurately during deserialization.

Hint 3
We can use the Depth First Search (DFS) algorithm for both serialization and deserialization. During serialization, we traverse the tree and add node values to the result string separated by a delimiter, inserting N whenever we encounter a null node. During deserialization, we process the serialized string using an index i, create nodes for valid values, and return from the current path whenever we encounter N, reconstructing the tree accurately.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
