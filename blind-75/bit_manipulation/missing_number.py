'''
Missing Number
Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.

Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Example 1:

Input: nums = [1,2,3]

Output: 0
Explanation: Since there are 3 numbers, the range is [0,3]. The missing number is 0 since it does not appear in nums.

Example 2:

Input: nums = [0,2]

Output: 1
Constraints:

1 <= nums.length <= 1000

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.

Hint 1
A brute force approach would iterate through the range of numbers from 0 to n, checking if each number is present in the given array. If a number is missing, it is returned. This results in an O(n^2) solution. Can you think of a better way? Maybe a data structure could help optimize this process.

Hint 2
We can use a hash set by inserting the given array elements into it. Then, we iterate through the range of numbers from 0 to n and use the hash set for O(1) lookups to find the missing number. Can you think of a way to further optimize this? Maybe a bitwise operator could be useful.

Hint 3
We can use bitwise XOR. When two identical numbers are XORed, the result is 0. Using this property, we can efficiently find the missing number.

Hint 4
We first compute the bitwise XOR of numbers from 0 to n. Then, we iterate through the array and XOR its elements as well. The missing number remains in the final XOR result since all other numbers appear twice—once in the range and once in the array—while the missing number is XORed only once.
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        