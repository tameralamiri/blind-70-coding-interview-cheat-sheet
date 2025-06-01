'''
Counting Bits
Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].

Return an array output where output[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 4

Output: [0,1,1,2,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100

Constraints:

0 <= n <= 1000

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the given integer.

Hint 1
A straightforward approach would be to iterate from 0 to n using i, and for each i, iterate through its bits to count the number of set bits. This would result in an O(n \log n) approach. Can you think of a better way? Maybe you should try identifying a pattern by observing the bitwise representation of consecutive numbers.

Hint 2
For example, to compute set bits for 7, add 1 to the count of set bits in 3, which was previously computed by adding 1 to the count of set bits in 1. Observing the pattern, for numbers less than 4, add 1 to the count from two positions before. For numbers less than 8, add 1 to the count from four positions before. Can you derive a dynamic programming relation from this?

Hint 3
We find an offset for the current number based on the number before offset positions. The dynamic programming relation is dp[i] = 1 + dp[i - offset], where dp[i] represents the number of set bits in i. The offset starts at 1 and updates when encountering a power of 2. To simplify the power of 2 check, if offset * 2 equals the current number, we update offset to the current number.
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        