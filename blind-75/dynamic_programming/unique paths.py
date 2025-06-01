'''
Unique Paths
There is an m x n grid where you are allowed to move either down or to the right at any point in time.

Given the two integers m and n, return the number of possible unique paths that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).

You may assume the output will fit in a 32-bit integer.

Example 1:



Input: m = 3, n = 6

Output: 21
Example 2:

Input: m = 3, n = 3

Output: 6
Constraints:

1 <= m, n <= 100

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(m * n) time and O(m * n) space, where m is the number of rows and n is the number of columns in the grid.

Hint 1
Try to think in terms of recursion and visualize it as a decision tree, where we have two choices at each step. Can you determine the base condition and recurrence relation?

Hint 2
We recursively traverse the grid using row i and column j. At each step, we explore both possibilities: moving down or moving right, ensuring we do not go out of bounds. If we reach the bottom-right cell, we return 1.

Hint 3
This approach has exponential complexity. Can you think of a way to optimize the recursion? Maybe you should consider using a dynamic programming approach.

Hint 4
We can use memoization to cache the results of recursive calls and avoid recalculations. A hash map or a 2D array can be used to store these results.
'''