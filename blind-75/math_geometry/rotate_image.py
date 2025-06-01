'''
Rotate Image
Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.

You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.

Example 1:



Input: matrix = [
  [1,2],
  [3,4]
]

Output: [
  [3,1],
  [4,2]
]
Example 2:



Input: matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

Output: [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

Recommended Time & Space Complexity
You should aim for a solution with O(n^2) time and O(1) space, where n is the length of the side of the given square matrix.

Hint 1
A brute force approach would use O(n^2) extra space to solve the problem. Can you think of a way to avoid using extra space? Maybe you should consider observing the positions of the elements before rotating and after rotating of the matrix.

Hint 2
We can rotate the matrix in two steps. First, we reverse the matrix vertically, meaning the first row becomes the last, the second row becomes the second last, and so on. Next, we transpose the reversed matrix, meaning rows become columns and columns become rows. How would you transpose the matrix?

Hint 3
Since the given matrix is a square matrix, we only need to iterate over the upper triangular part, meaning the right upper portion of the main diagonal. In this way, we can transpose a matrix.
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        