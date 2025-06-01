'''
Longest Increasing Subsequence
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".
Example 1:

Input: nums = [9,1,4,2,3,3,7]

Output: 4
Explanation: The longest increasing subsequence is [1,2,3,7], which has a length of 4.

Example 2:

Input: nums = [0,3,1,3,2,3]

Output: 4
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n ^ 2) time and O(n ^ 2) space, where n is the size of the input array.

Hint 1
A subsequence is formed by selecting elements while maintaining their order. Using recursion, we can generate all subsequences. The recursive function returns the length of the longest increasing subsequence up to index i, processing from left to right. At each step, we decide whether to include or exclude the current element.

Hint 2
Since the sequence must be increasing, we represent choices by adding 1 when including an element and 0 when excluding it. In recursion, how can we ensure the current element is greater than the previous one? Perhaps additional information is needed to process it.

Hint 3
We can store the index of the previously chosen element as j, making it easier to process the current element at index i. If and only if j == -1 or nums[i] > nums[j], we include the current element and extend the recursive path. Can you determine the recurrence relation? At most, two recursive calls are made at each recursion step.

Hint 4
We stop the recursion when index i goes out of bounds and return 0 since no more elements can be added. The initial recursion call starts with j = -1. At each step, we include the current element if it is greater than the previous one and continue the recursion, or we exclude it and explore the next possibility. We return the maximum value obtained from both paths.

Hint 5
The time complexity of this approach is exponential. We can use memoization to store results of recursive calls and avoid recalculations. A hash map or a 2D array can be used to cache these results.
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        