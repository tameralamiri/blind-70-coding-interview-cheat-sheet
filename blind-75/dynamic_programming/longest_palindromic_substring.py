'''
Longest Palindromic Substring
Given a string s, return the longest substring of s that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.

Example 1:

Input: s = "ababd"

Output: "bab"
Explanation: Both "aba" and "bab" are valid answers.

Example 2:

Input: s = "abbc"

Output: "bb"
Constraints:

1 <= s.length <= 1000
s contains only digits and English letters.

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n^2) time and O(1) space, where n is the length of the given string.

Hint 1
A brute-force solution would be to check if every substring is a palindrome and return the maximum length among all the palindromic substring lengths. This would be an O(n^3) time solution. Can you think of a better way? Perhaps you should consider thinking in terms of the center of a palindrome.

Hint 2
Iterate over the string with index i and treat the current character as the center. For this character, try to extend outward to the left and right simultaneously, but only if both characters are equal. Update the result variable accordingly. How would you implement this? Can you consider both cases: even-length and odd-length palindromes?

Hint 3
Maintain two variables, resLen and res, which denote the length of the longest palindrome and the start index of that palindrome, respectively. At each index, you can create an odd-length palindrome starting at that index extending outward from both its left and right indices, i.e., i - 1 and i + 1. How can you find the even-length palindrome for this index?

Hint 4
For an even-length palindrome, consider expanding from indices i and i + 1. This two-pointer approach, extending from the center of the palindrome, will help find all palindromic substrings in the given string. Update the two result variables and return the substring starting at res with a length of resLen.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        