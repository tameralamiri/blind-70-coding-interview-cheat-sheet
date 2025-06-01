'''
Linked List Cycle Detection

Easy

Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.

Example 1:

1 -> 2 -> 3 -> 4
     ^         |
     | - - - - v

Input: head = [1,2,3,4], index = 1

Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

1 -> 2

Input: head = [1,2], index = -1

Output: false
Constraints:

1 <= Length of the list <= 1000.
-1000 <= Node.val <= 1000
index is -1 or a valid index in the linked list.

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(1) space, where n is the length of the given list.

Hint 1
A naive approach would be to use a hash set, which takes O(1) time to detect duplicates. Although this solution is acceptable, it requires O(n) extra space. Can you think of a better solution that avoids using extra space? Maybe there is an efficient algorithm which uses two pointers.

Hint 2
We can use the fast and slow pointers technique, which is primarily used to detect cycles in a linked list. We iterate through the list using two pointers. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If the list has a cycle, these two pointers will eventually meet. Why does this work?

Hint 3
When there is no cycle in the list, the loop ends when the fast pointer becomes null. If a cycle exists, the fast pointer moves faster and continuously loops through the cycle. With each step, it reduces the gap between itself and the slow pointer by one node. For example, if the gap is 10, the slow pointer moves by 1, increasing the gap to 11, while the fast pointer moves by 2, reducing the gap to 9. This process continues until the fast pointer catches up to the slow pointer, confirming a cycle.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        