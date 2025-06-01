'''
Spiral Matrix
Given an m x n matrix of integers matrix, return a list of all elements within the matrix in spiral order.

Example 1:



Input: matrix = [[1,2],[3,4]]

Output: [1,2,4,3]
Example 2:



Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output: [1,2,3,6,9,8,7,4,5]
Example 3:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

Output: [1,2,3,4,8,12,11,10,9,5,6,7]
Constraints:

1 <= matrix.length, matrix[i].length <= 10
-100 <= matrix[i][j] <= 100

Recommended Time & Space Complexity
You should aim for a solution with O(m*n) time and O(1) extra space, where m is the number of rows and n is the number of columns in the given matrix.

Hint 1
Try to simulate the process as described in the problem. Think in terms of matrix layers, starting from the outermost boundaries and moving inward. Can you determine an efficient way to implement this?

Hint 2
Each boundary consists of four parts: the top row, right column, bottom row, and left column, which follow the spiral order and act as four pointers. For each layer, the top pointer increments by one, the right pointer decrements by one, the left pointer increments by one, and the bottom pointer decrements by one.

Hint 3
At each layer, four loops traverse the matrix: one moves left to right along the top row, another moves top to bottom along the right column, the next moves right to left along the bottom row, and the last moves bottom to top along the left column. This process generates the spiral order.
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        