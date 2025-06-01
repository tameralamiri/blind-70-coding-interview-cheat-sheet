'''
Maximum Product Subarray
Given an integer array nums, find a subarray that has the largest product within the array and return it.

A subarray is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a 32-bit integer.

Example 1:

Input: nums = [1,2,-3,4]

Output: 4
Example 2:

Input: nums = [-2,-1]

Output: 2
Constraints:

1 <= nums.length <= 1000
-10 <= nums[i] <= 10

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.


Hint 1
A brute force solution would be to find the product for every subarray and then return the maximum among all the products. This would be an O(n ^ 2) approach. Can you think of a better way? Maybe you should think of a dynamic programming approach.

Hint 2
Try to identify a pattern by finding the maximum product for an array with two elements and determining what values are needed when increasing the array size to three. Perhaps you only need two values when introducing a new element.

Hint 3
We maintain both the minimum and maximum product values and update them when introducing a new element by considering three cases: starting a new subarray, multiplying with the previous max product, or multiplying with the previous min product. The max product is updated to the maximum of these three, while the min product is updated to the minimum. We also track a global max product for the result. This approach is known as Kadane's algorithm.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        