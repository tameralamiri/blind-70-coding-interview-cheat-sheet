'''
Remove Node From End of Linked List

Medium

You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.

Example 1:

Input: head = [1,2,3,4], n = 2

Output: [1,2,4]
Example 2:

Input: head = [5], n = 1

Output: []
Example 3:

Input: head = [1,2], n = 2

Output: [2]
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Recommended Time & Space Complexity
You should aim for a solution with O(N) time and O(1) space, where N is the length of the given list.

Hint 1
A brute force solution would involve storing the nodes of the list into an array, removing the nth node from the array, and then converting the array back into a linked list to return the new head. However, this requires O(N) extra space. Can you think of a better approach to avoid using extra space? Maybe you should first solve with a two pass approach.

Hint 2
We can use a two-pass approach by first finding the length of the list, N. Since removing the nth node from the end is equivalent to removing the (N - n)th node from the front, as they both mean the same. How can you remove the node in a linked list?

Hint 3
For example, consider a three-node list [1, 2, 3]. If we want to remove 2, we update the next pointer of 1 (initially pointing to 2) to point to the node after 2, which is 3. After this operation, the list becomes [1, 3], and we return the head. But, can we think of a more better approach? Maybe a greedy calculation can help.

Hint 4
We can solve this in one pass using a greedy approach. Move the first pointer n steps ahead. Then, start another pointer second at the head and iterate both pointers simultaneously until first reaches null. At this point, the second pointer is just before the node to be removed. We then remove the node that is next to the second pointer. Why does this work?

Hint 5
This greedy approach works because the second pointer is n nodes behind the first pointer. When the first pointer reaches the end, the second pointer is exactly n nodes from the end. This positioning allows us to remove the nth node from the end efficiently.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        