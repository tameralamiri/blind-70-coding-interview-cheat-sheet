'''
Jump Game
You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.

Return true if you can reach the last index starting from index 0, or false otherwise.

Example 1:

Input: nums = [1,2,0,1,0]

Output: true
Explanation: First jump from index 0 to 1, then from index 1 to 3, and lastly from index 3 to 4.

Example 2:

Input: nums = [1,2,1,0,1]

Output: false
Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(1) space, where n is the size of input array.

Hint 1
A brute force approach would be to recursively explore all paths from index 0 to its reachable indices, then process those indices similarly, returning true if we reach the last index. This would be an exponential approach. Can you think of a better way? Maybe a greedy approach works.

Hint 2
Instead of processing the array from index 0, start from the last index. Let the target index be goal = n - 1. Iterate in reverse from index n - 2.

Hint 3
At each iteration, we check whether the current index can reach goal. If it can, we update goal to the current index, as reaching the current index means we can also reach the goal.

Hint 4
To determine if we can reach the last index, the goal should be 0 after the iteration. Otherwise, reaching the last index is not possible.
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        