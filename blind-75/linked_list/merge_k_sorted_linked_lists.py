'''
Merge K Sorted Linked Lists: 

Hard

You are given an array of k linked lists lists, where each list is sorted in ascending order.

Return the sorted linked list that is the result of merging all of the individual linked lists.

Example 1:

Input: lists = [[1,2,4],[1,3,5],[3,6]]

Output: [1,1,2,3,3,4,5,6]
Example 2:

Input: lists = []

Output: []
Example 3:

Input: lists = [[]]

Output: []
Constraints:

0 <= lists.length <= 1000
0 <= lists[i].length <= 100
-1000 <= lists[i][j] <= 1000

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n * k) time and O(1) space, where k is the total number of lists and n is the total number of nodes across all lists.

Hint 1
A brute-force solution would involve storing all n nodes in an array, sorting them, and converting the array back into a linked list, resulting in an O(nlogn) time complexity. Can you think of a better way? Perhaps consider leveraging the idea behind merging two sorted linked lists.

Hint 2
We can merge two sorted linked lists without using any extra space. To handle k sorted linked lists, we can iteratively merge each linked list with a resultant merged list. How can you implement this?

Hint 3
We iterate through the list array with index i, starting at i = 1. We merge the linked lists using mergeTwoLists(lists[i], lists[i - 1]), which returns the head of the merged list. This head is stored in lists[i], and the process continues. Finally, the merged list is obtained at the last index, and we return its head.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        