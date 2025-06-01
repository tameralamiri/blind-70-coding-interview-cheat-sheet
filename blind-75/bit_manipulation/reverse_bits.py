'''
Reverse Bits
Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

Example 1:

Input: n = 00000000000000000000000000010101

Output:    2818572288 (10101000000000000000000000000000)
Explanation: Reversing 00000000000000000000000000010101, which represents the unsigned integer 21, gives us 10101000000000000000000000000000 which represents the unsigned integer 2818572288.

Recommended Time & Space Complexity
You should aim for a solution with O(1) time and O(1) space.

Hint 1
Given a 32-bit integer, what is the position of bit i after reversing the bits? Maybe you should observe the bit positions before and after reversal to find a pattern.

Hint 2
After reversing the bits, the bit at position i moves to position 31 - i. Can you use this observation to construct the reversed number efficiently?

Hint 3
We initialize res to 0 and iterate through the bits of the given integer n. We extract the bit at the i-th position using ((n >> i) & 1). If it is 1, we set the corresponding bit in res at position (31 - i) using (res |= (1 << (31 - i))).
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        