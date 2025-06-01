'''
Meeting Rooms II
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Note:

(0,8),(8,10) is not considered a conflict at 8
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000

Recommended Time & Space Complexity
You should aim for a solution with O(nlogn) time and O(n) space, where n is the size of the input array.

Hint 1
Try to visualize the meetings as line segments on a number line representing start and end times. The number of rooms required is the maximum number of overlapping meetings at any point on the number line. Can you think of a way to determine this efficiently?

Hint 2
We create two arrays, start and end, containing the start and end times of all meetings, respectively. After sorting both arrays, we use a two-pointer based approach. How do you implement this?

Hint 3
We use two pointers, s and e, for the start and end arrays, respectively. We also maintain a variable count to track the current number of active meetings. At each iteration, we increment s while the start time is less than the current end time and increase count, as these meetings must begin before the earliest ongoing meeting ends.

Hint 4
Then, we increment e and decrement count as a meeting has ended. At each step, we update the result with the maximum value of active meetings stored in count.
'''
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        