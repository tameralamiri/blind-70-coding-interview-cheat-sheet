'''
Longest Common Subsequence
Given two strings text1 and text2, return the length of the longest common subsequence between the two strings if one exists, otherwise return 0.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".
A common subsequence of two strings is a subsequence that exists in both strings.

Example 1:

Input: text1 = "cat", text2 = "crabt" 

Output: 3 
Explanation: The longest common subsequence is "cat" which has a length of 3.

Example 2:

Input: text1 = "abcd", text2 = "abcd"

Output: 4
Example 3:

Input: text1 = "abcd", text2 = "efgh"

Output: 0
Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(m * n) time and O(m * n) space, where m is the length of the string text1 and n is the length of the string text2.

Hint 1
Try to think in terms of recursion and visualize it as a decision tree. Can you determine the possible decisions at each step? Maybe you should consider iterating through both strings recursively at the same time.

Hint 2
At each recursion step, we have two choices: if the characters at the current indices of both strings match, we move both indices forward and extend the subsequence. Otherwise, we explore two paths by advancing one index at a time and recursively finding the longest subsequence. We return the maximum length between these two choices. This approach is exponential. Can you think of a way to optimize it?

Hint 3
We return 0 if either index goes out of bounds. To optimize, we can use memoization to cache recursive call results and avoid redundant calculations. A hash map or a 2D array can be used to store these results.
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        