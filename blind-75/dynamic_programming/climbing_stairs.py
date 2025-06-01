'''
Climbing Stairs
You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

Example 1:

Input: n = 2

Output: 2
Explanation:

1 + 1 = 2
2 = 2
Example 2:

Input: n = 3

Output: 3
Explanation:

1 + 1 + 1 = 3
1 + 2 = 3
2 + 1 = 3

Constraints:
1 <= n <= 30

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n) time and O(n) space, where n is the number of steps.

Hint 1
At each step, we have two choices: climb one step or climb two steps. We can solve this by considering both options and picking the minimum using recursion. However, this results in O(2^n) time complexity. Can you think of a better approach? Perhaps, try to avoid the repeated work of calling recursion more than once with same parameters.

Hint 2
This is a Dynamic Programming problem. We can use Memoization to avoid repeated work. Create an n-sized array cache to store the results of recursive calls. When the recursion is called with specific parameters, return the stored value if it has already been computed. How would you implement this?

Hint 3
We start the initial recursion with i = 0, indicating that we are at position i. We first check if the current recursion with the given i is already cached. If it is, we immediately return the stored value. Otherwise, we perform the recursion, store the result in the cache, and then return it. Can you think of the base condition to stop the recursion?

Hint 4
At each recursion, we perform two recursive calls: one for climbing one step and another for climbing two steps. The minimum return value between the two is the result for the current recursion. The base condition is to return 0 if i == n. This is a one-dimensional dynamic programming problem, which can be further optimized using more advanced techniques.
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        