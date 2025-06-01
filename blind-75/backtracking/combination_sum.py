'''
Combination Sum
You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:

Input: 
nums = [2,5,6,9] 
target = 9

Output: [[2,2,5],[9]]
Explanation:
2 + 2 + 5 = 9. We use 2 twice, and 5 once.
9 = 9. We use 9 once.

Example 2:

Input: 
nums = [3,4,5]
target = 16

Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]
Example 3:

Input: 
nums = [3]
target = 5

Output: []
Constraints:

All elements of nums are distinct.
1 <= nums.length <= 20
2 <= nums[i] <= 30
2 <= target <= 30


Recommended Time & Space Complexity
You should aim for a solution with O(2^(t/m)) time and O(t/m) space, where t is the given target and m is the minimum value in the given array.

Hint 1
Can you think of this problem in terms of a decision tree, where at each step, we have n decisions, where n is the size of the array? In this decision tree, we can observe that different combinations of paths are formed. Can you think of a base condition to stop extending a path? Maybe you should consider the target value.

Hint 2
We can use backtracking to recursively traverse these paths and make decisions to choose an element at each step. We maintain a variable sum, which represents the sum of all the elements chosen in the current path. We stop this recursive path if sum == target, and add a copy of the chosen elements to the result. How do you implement it?

Hint 3
We recursively traverse the array starting from index i. At each step, we select an element from i to the end of the array. We extend the recursive path with elements where sum <= target after including that element. This creates multiple recursive paths, and we append the current list to the result whenever the base condition is met.
'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        