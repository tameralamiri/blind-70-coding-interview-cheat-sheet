'''
Decode Ways
A string consisting of uppercase english characters can be encoded to a number using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping above. There may be multiple ways to decode a message. For example, "1012" can be mapped into:

"JAB" with the grouping (10 1 2)
"JL" with the grouping (10 12)
The grouping (1 01 2) is invalid because 01 cannot be mapped into a letter since it contains a leading zero.

Given a string s containing only digits, return the number of ways to decode it. You can assume that the answer fits in a 32-bit integer.

Example 1:

Input: s = "12"

Output: 2

Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "01"

Output: 0
Explanation: "01" cannot be decoded because "01" cannot be mapped into a letter.

Constraints:

1 <= s.length <= 100
s consists of digits

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n) time and O(n) space, where n is the length of the given string.

Hint 1
The characters A through Z are mapped to the numbers from 1 to 26. A mapped number can have at most 2 digits. In the given string of digits, we can explore all possible decodings by combining one or two consecutive digits. Think of this in terms of a decision tree and explore all paths. Can you derive a recurrence relation for this?

Hint 2
Iterate over the string with index i. At each index, we have two choices: decode the current digit as a character with its mapped value, or combine the current digit with the next digit to form a two-digit value. The recurrence relation can be expressed as dfs(i + 1) + dfs(i + 2) where dfs is the recursive function. Also, consider edge cases, as not every two-digit number or a number with a leading zero is valid. How would you implement this?

Hint 3
A brute-force recursive solution would result in O(2^n) time complexity. Can you think of a better way? Perhaps you should consider the repeated work of calling the recursion multiple times with the same parameter values and find a way to avoid this. Also, can you think about the base condition of this recursive function?

Hint 4
The base condition is to return 1 if i goes out of bounds. If the current digit is '0', return 0, as no character maps to '0', making the string invalid. Use memoization to avoid repeated work by caching recursion results in an array or hash map and returning the stored value when the result is already calculated.
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        