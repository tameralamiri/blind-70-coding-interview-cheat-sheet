'''
Coin Change
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.

You may assume that you have an unlimited number of each coin.

Example 1:

Input: coins = [1,5,10], amount = 12

Output: 3
Explanation: 12 = 10 + 1 + 1. Note that we do not have to use every kind coin available.

Example 2:

Input: coins = [2], amount = 3

Output: -1
Explanation: The amount of 3 cannot be made up with coins of 2.

Example 3:

Input: coins = [1], amount = 0

Output: 0
Explanation: Choosing 0 coins is a valid way to make up 0.

Constraints:

1 <= coins.length <= 10
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10000


Recommended Time & Space Complexity
You should aim for a solution with O(n * t) time and O(t) space, where n is the number of coins and t is the given amount.

Hint 1
Think of this problem in terms of recursion and try to visualize the decision tree, as there are multiple choices at each step. We start with the given amount. At each step of recursion, we have n coins and branch into paths using coins that are less than or equal to the current amount. Can you express this in terms of a recurrence relation? Also, try to determine the base condition to stop the recursion.

Hint 2
If the amount is 0, we return 0 coins. The recurrence relation can be expressed as min(1 + dfs(amount - coins[i])), where we return the minimum coins among all paths. This results in an O(n ^ t) solution, where n is the number of coins and t is the total amount. Can you think of a better approach? Perhaps consider the repeated work and find a way to avoid it.

Hint 3
We can use memoization to avoid the repeated work of calculating the result for each recursive call. A hash map or an array of size t can be used to cache the computed values for a specific amount. At each recursion step, we iterate over every coin and extend only the valid paths. If a result has already been computed, we return it from the cache instead of recalculating it.
'''