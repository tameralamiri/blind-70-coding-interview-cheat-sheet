'''
Set Matrix Zeroes

Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

You must update the matrix in-place.

Follow up: Could you solve it using O(1) space?

Example 1:



Input: matrix = [
  [0,1],
  [1,0]
]

Output: [
  [0,0],
  [0,0]
]
Example 2:



Input: matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]

Output: [
  [1,0,3],
  [0,0,0],
  [6,0,8]
]
Constraints:

1 <= matrix.length, matrix[0].length <= 100
-2^31 <= matrix[i][j] <= (2^31) - 1

Recommended Time & Space Complexity
You should aim for a solution with O(m*n) time and O(1) space, where m is the number of rows and n is the number of columns in the given matrix.

Hint 1
A brute force approach would iterate through the given matrix and update the corresponding row and column in a new matrix on the fly. This would result in an O((m*n)*(m+n)) time and O(m*n) space solution. Can you think of a better way? Maybe you should consider using a single variable for a row and a single variable for a column instead of updating entire row and column.

Hint 2
A better approach is to use O(m+n) boolean arrays. We iterate through the matrix, and when encountering a zero, we mark the respective row and column as true. In the second iteration, we set a cell to 0 if its corresponding row or column is marked true. Can you think of a way to optimize the space further?

Hint 3
We can use the topmost row and leftmost column of the matrix as boolean arrays by marking 0 instead of true. However, since they overlap at one cell, we use a single variable to track the top row separately. We then iterate through the matrix and mark zeros accordingly.

Hint 4
In the second iteration, we update all cells that are not part of the top row or left column accordingly. After making the necessary changes, we check the top-leftmost cell and update the corresponding column. Finally, we check the extra variable and update the top row accordingly.
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None: