'''
Insert Interval
You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents the start and the end time of the ith interval. intervals is initially sorted in ascending order by start_i.

You are given another interval newInterval = [start, end].

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

Return intervals after adding newInterval.

Note: Intervals are non-overlapping if they have no common point. For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

Example 1:

Input: intervals = [[1,3],[4,6]], newInterval = [2,5]

Output: [[1,6]]
Example 2:

Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]

Output: [[1,2],[3,5],[6,7],[9,10]]
Constraints:

0 <= intervals.length <= 1000
newInterval.length == intervals[i].length == 2
0 <= start <= end <= 1000

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(1) extra space, where n is the size of the input array.

Hint 1
The given intervals are non-overlapping and sorted in ascending order based on the start value. Try to visualize them as line segments and consider how a new interval can be inserted. Maybe you should analyze different cases of inserting a new interval.

Hint 2
First, we append all intervals to the output list that have an end value smaller than the start value of the new interval. Then, we encounter one of three cases: we have appended all intervals, we reach an interval whose start value is greater than the new interval’s end, or we find an overlapping interval. Can you think of a way to handle these cases efficiently?

Hint 3
We iterate through the remaining intervals, updating the new interval if its end value is greater than or equal to the current interval's start value. We adjust the start and end of the new interval to the minimum and maximum values, respectively. After this, any remaining intervals are appended to the output list, and we return the result.
'''