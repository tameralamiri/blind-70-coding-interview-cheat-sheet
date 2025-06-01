'''
Maximum Subarray
Given an array of integers nums, find the subarray with the largest sum and return the sum.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [2,-3,4,-2,2,1,-1,4]

Output: 8
Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.

Example 2:

Input: nums = [-1]

Output: -1
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.

Hint 1
A brute force approach would be to compute the sum of every subarray and return the maximum among them. This would be an O(n^2) approach. Can you think of a better way? Maybe you should consider a dynamic programming-based approach.

Hint 2
Instead of calculating the sum for every subarray, try maintaining a running sum. Maybe you should consider whether extending the previous sum or starting fresh with the current element gives a better result. Can you think of a way to track this efficiently?

Hint 3
We use a variable curSum to track the sum of the elements. At each index, we have two choices: either add the current element to curSum or start a new subarray by resetting curSum to the current element. Maybe you should track the maximum sum at each step and update the global maximum accordingly.

Hint 4
This algorithm is known as Kadane's algorithm.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        