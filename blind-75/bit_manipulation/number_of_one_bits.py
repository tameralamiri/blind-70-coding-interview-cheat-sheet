'''
Number of One Bits
You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

You may assume n is a non-negative integer which fits within 32-bits.

Example 1:

Input: n = 00000000000000000000000000010111

Output: 4
Example 2:

Input: n = 01111111111111111111111111111101

Output: 30

Recommended Time & Space Complexity
You should aim for a solution with O(1) time and O(1) space.

Hint 1
The given integer is a 32-bit integer. Can you think of using bitwise operators to iterate through its bits? Maybe you should consider iterating 32 times.

Hint 2
We iterate 32 times (0 to 31) using index i. The expression (1 << i) creates a bitmask with a set bit at the i-th position. How can you check whether the i-th bit is set in the given number? Maybe you should consider using the bitwise-AND ("&").

Hint 3
Since the mask has a set bit at the i-th position and all 0s elsewhere, we can perform a bitwise-AND with n. If n has a set bit at the i-th position, the result is positive; otherwise, it is 0. We increment the global count if the result is positive and return it after the iteration.
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        