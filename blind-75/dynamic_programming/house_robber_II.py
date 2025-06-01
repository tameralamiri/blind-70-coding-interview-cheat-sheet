'''
House Robber II
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:

Input: nums = [3,4,3]

Output: 4
Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2] are adjacent houses. The maximum you can rob is nums[1] = 4.

Example 2:

Input: nums = [2,9,8,3,6]

Output: 15
Explanation: You cannot rob nums[0] + nums[2] + nums[4] = 16 because nums[0] and nums[4] are adjacent houses. The maximum you can rob is nums[1] + nums[4] = 15.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n) time and O(n) space, where n is the number of houses.

Hint 1
First, consider solving the problem to get the maximum money after robbing without the condition that 'the first and last houses are adjacent'. Can you express this using a recurrence relation? Perhaps you could draw a decision tree, as at each step, you can either rob the current house and skip the next one or skip the current house and move to the next.

Hint 2
The recurrence relation can be expressed as max(nums[i] + dfs(i + 2), dfs(i + 1)), where i is the current house and dfs is the recursive function. The base condition for this recursion would be to return 0 when i goes out of bounds. This solution results in O(2^n) time complexity because, at each recursive step, we branch into two paths. Can you think of a way to avoid recalculating the result for the same recursive call multiple times?

Hint 3
We can use memoization to store the result of a recursive function in a hash map or an array and immediately return this value when the function is called again with the same parameter values. How would you implement this? How would you solve the problem if the first and last houses are adjacent to each other? Perhaps you should consider skipping any one house between the two.

Hint 4
We can create two arrays from the given array. The first will include houses from the first house to the second-to-last house, and the second will include houses from the second house to the last house. We can run the recursive function on both arrays independently and return the maximum result between the two. Advanced techniques such as bottom-up dynamic programming can further optimize the solution.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        