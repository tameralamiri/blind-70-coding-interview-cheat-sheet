'''
Minimum Window Substring
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"
Example 3:

Input: s = "x", t = "xy"

Output: ""
Constraints:

1 <= s.length <= 1000
1 <= t.length <= 1000
s and t consist of uppercase and lowercase English letters.

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(m) space, where n is the length of the string s and m is the number of unique characters in s and t.

Hint 1
A brute force solution would involve checking every substring of s against t and returning the minimum length valid substring. This would be an O(n^2) solution. Can you think of a better way? Maybe you should think in terms of frequency of characters.

Hint 2
We need to find substrings in s that should have atleast the characters of t. We can use hash maps to maintain the frequencies of characters. It will be O(1) for lookups. Can you think of an algorithm now?

Hint 3
We can use a dynamically sized sliding window approach on s. We iterate through s while maintaining a window. If the current window contains at least the frequency of characters from t, we update the result and shrink the window until it is valid.

Hint 4
We should ensure that we maintain the result substring and only update it if we find a shorter valid substring. Additionally, we need to keep track of the result substring's length so that we can return an empty string if no valid substring is found.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        