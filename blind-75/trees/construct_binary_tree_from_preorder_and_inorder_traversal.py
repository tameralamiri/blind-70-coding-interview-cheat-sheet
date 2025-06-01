'''
Construct Binary Tree from Preorder and Inorder Traversal
You are given two integer arrays preorder and inorder.

preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.

Example 1:



Input: preorder = [1,2,3,4], inorder = [2,1,3,4]

Output: [1,2,3,null,null,null,4]
Example 2:

Input: preorder = [1], inorder = [1]

Output: [1]
Constraints:

1 <= inorder.length <= 1000.
inorder.length == preorder.length
-1000 <= preorder[i], inorder[i] <= 1000

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes.

Hint 1
You can observe that the in-order traversal helps divide the array into two halves based on the root node: the left part corresponds to the left subtree, and the right part corresponds to the right subtree. Can you think of how we can get the index of the root node in the in-order array? Maybe you should look into the pre-order traversal array.

Hint 2
From the pre-order traversal, we know that the first node is the root node. Using this information, can you now construct the binary tree?

Hint 3
After getting the root node from pre-order traversal, we then look for the index of that node in the in-order array. We can linearly search for the index but this would be an O(n^2) solution. Can you think of a better way? Maybe we can use a data structure to get the index of a node in O(1)?

Hint 4
We can use a hash map to get the index of any node in the in-order array in O(1) time. How can we implement this?

Hint 5
We use Depth First Search (DFS) to construct the tree. A global variable tracks the current index in the pre-order array. Indices l and r represent the segment in the in-order array for the current subtree. For each node in the pre-order array, we create a node, find its index in the in-order array using the hash map, and recursively build the left and right subtrees by splitting the range [l, r] into two parts for the left and right subtrees.
'''