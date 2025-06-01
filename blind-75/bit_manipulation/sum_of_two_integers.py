'''
Sum of Two Integers
Given two integers a and b, return the sum of the two integers without using the + and - operators.

Example 1:

Input: a = 1, b = 1

Output: 2
Example 2:

Input: a = 4, b = 7

Output: 11
Constraints:

-1000 <= a, b <= 1000

Recommended Time & Space Complexity
You should aim for a solution with O(1) time and O(1) space.

Hint 1
A brute force approach would use the addition operator. Can you think of a way to perform addition without using it? Maybe you should consider solving this using bit manipulation.

Hint 2
We can use the bitwise XOR operator to perform addition. If both a and b have 1 at the same bit position, the sum at that position is 0, and a carry of 1 is generated. If the bits are different, the sum at that position is 1. Additionally, we account for the carry from the previous step in the next iteration.

Hint 3
We iterate bit by bit from 0 to 31 since the given integers are 32-bit. We track the carry, initially set to 0, and initialize the result as res. During iteration, the XOR of the bits at the i-th position of both integers and the carry determines the current bit of res. How can you handle negative numbers?

Hint 4
To handle negative numbers, if the final result exceeds the maximum positive 32-bit integer, it means the number should be negative. We adjust it using bitwise operations: flipping the bits with res ^ ((2 ^ 32) - 1) and applying ~ to restore the correct two’s complement representation. This ensures the result correctly represents signed 32-bit integers.
'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        