'''
Valid Parentheses
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the length of the given string.

Hint 1
A brute force solution would be to continuously remove valid brackets until no more can be removed. If the remaining string is empty, return true; otherwise, return false. This would result in an O(n^2) solution. Can we think of a better approach? Perhaps a data structure could help.

Hint 2
We can use a stack to store characters. Iterate through the string by index. For an opening bracket, push it onto the stack. If the bracket is a closing type, check for the corresponding opening bracket at the top of the stack. If we don't find the corresponding opening bracket, immediately return false. Why does this work?

Hint 3
In a valid parenthesis expression, every opening bracket must have a corresponding closing bracket. The stack is used to process the valid string, and it should be empty after the entire process. This ensures that there is a valid substring between each opening and closing bracket.
'''

# The Engineering Method:
#################################################
# 1. Explore
# Understand the Problem:

# Input: A string s with only '(', ')', '{', '}', '[' and ']'.
# Output: Return True if the string is a valid parentheses sequence, False otherwise.
# Examples:

# "[]" → True
# "([{}])" → True
# "[(])" → False
# Constraints:

# 1 ≤ s.length ≤ 1000
#################################################
# 2. BrainStorm
# Naive Approach:

# Remove pairs of valid brackets until no more can be removed.
# If the string is empty at the end, it's valid.
# Downside: O(n²) time.
# Better Approach:

# Use a stack:
# Push opening brackets onto the stack.
# For closing brackets, check if the top of the stack is the matching opening bracket.
# If not, return False.
# At the end, the stack should be empty.
# Why Stack?

# Stack helps track the most recent opening bracket, matching the required closing order.
#################################################
# 3. Plan
# Algorithm:

# Create a mapping of closing to opening brackets.
# Initialize an empty stack.
# Iterate through each character in the string:
# If it's an opening bracket, push to stack.
# If it's a closing bracket:
# If stack is empty or top of stack isn't the matching opening bracket, return False.
# Else, pop the stack.
# After iteration, if stack is empty, return True; else, False.
#################################################
# 4. Implement

class Solution:
    def is_valid(self, s: str) -> bool:
        closing_brackets = {'}': '{', ")" : "(", "]": "["}
        stack = []
        for char in s:
            if char in closing_brackets.values():
                stack.append(char)
            elif char in closing_brackets:
                if not stack or stack[-1] != closing_brackets[char]:
                    return False
                stack.pop()
        return not stack

#################################################
# 5. Verify
sol = Solution()
assert sol.is_valid("[]") == True
assert sol.is_valid("([{}])") == True
assert sol.is_valid("[(])") == False
assert sol.is_valid("([)]") == False
assert sol.is_valid("{[]}") == True
assert sol.is_valid("(") == False
assert sol.is_valid("") == True

# Edge Cases:

# Single opening or closing bracket → False
# Empty string → True
# Nested and interleaved brackets → check correctness