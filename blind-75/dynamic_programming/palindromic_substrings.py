'''
Palindromic Substrings
Given a string s, return the number of substrings within s that are palindromes.

A palindrome is a string that reads the same forward and backward.

Example 1:

Input: s = "abc"

Output: 3
Explanation: "a", "b", "c".

Example 2:

Input: s = "aaa"

Output: 6
Explanation: "a", "a", "a", "aa", "aa", "aaa". Note that different substrings are counted as different palindromes even if the string contents are the same.

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n^2) time and O(1) space, where n is the length of the given string.

Hint 1
A brute-force solution would be to check if every substring is a palindrome and return the total number of palindromic substrings. This would be an O(n^3) time solution. Can you think of a better way? Perhaps you should consider thinking in terms of the center of a palindrome.

Hint 2
Iterate over the string with index i and treat the current character as the center. For this character, try to extend outward to the left and right simultaneously, but only if both characters are equal. At each iteration, we increment the count of palindromes. How would you implement this? Can you consider both cases: even-length and odd-length palindromes?

Hint 3
Initialize a variable res to track the count of palindromes. At each index, create an odd-length palindrome starting at that index extending outward from both its left and right indices, i.e., i - 1 and i + 1. How can you find the even-length palindrome for this index?

Hint 4
For an even-length palindrome, consider expanding from indices i and i + 1. This two-pointer approach, extending from the center of the palindrome, will help find all palindromic substrings in the given string and return its count.
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        