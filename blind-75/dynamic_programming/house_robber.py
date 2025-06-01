'''
House Robber
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:

Input: nums = [1,1,3,3]

Output: 4
Explanation: nums[0] + nums[2] = 1 + 3 = 4.

Example 2:

Input: nums = [2,9,8,3,6]

Output: 16
Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n) time and O(n) space, where n is the number of houses.

Hint 1
Can you think of this problem in terms of recursion? Consider drawing a decision tree where, at each step, we can choose to rob the house or skip it. If we rob the current house, we cannot rob the next or the previous house. Can you derive a recurrence relation to solve the problem?

Hint 2
We can recursively start from the first house and branch paths accordingly. If we rob the current house, we skip the next house; otherwise, we move to the next house. The recurrence relation can be expressed as max(nums[i] + dfs(i + 2), dfs(i + 1)), where i is the current house and dfs is the recursive function. Can you determine the base condition to stop the recursion?

Hint 3
The base condition would be to return 0 when i goes out of bounds. This recursion can leads to O(2^n) time solution. Can you think of a better way? Maybe you should try to avoid recalculating the result for a recursive call.

Hint 4
We can use Memoization to avoid recalculating the result multiple times for a recursive call. By storing the result of each recursive call in a hash map or an array using i as the parameter, we can immediately return the stored result if the recursion is called with the same i value again. Further optimization can be achieved using advanced techniques like Bottom-Up dynamic programming.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        