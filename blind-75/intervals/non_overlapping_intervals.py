'''
Non-overlapping Intervals
Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note: Intervals are non-overlapping even if they have a common point. For example, [1, 3] and [2, 4] are overlapping, but [1, 2] and [2, 3] are non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,4],[1,4]]

Output: 1
Explanation: After [1,4] is removed, the rest of the intervals are non-overlapping.

Example 2:

Input: intervals = [[1,2],[2,4]]

Output: 0
Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
-50000 <= starti < endi <= 50000

Recommended Time & Space Complexity
You should aim for a solution with O(nlogn) time and O(n) space, where n is the size of the input array.

Hint 1
If two intervals are sorted in ascending order by their start values, they overlap if the start value of the second interval is less than the end value of the first interval. And these are called overlapping intervals.

Hint 2
A brute force approach would be to sort the given intervals in ascending order based on their start values and recursively explore all possibilities. This would be an exponential approach. Can you think of a better way? Maybe a greedy approach works here.

Hint 3
We first sort the given intervals based on their start values to efficiently check for overlaps by comparing adjacent intervals. We then iterate through the sorted intervals from left to right, keeping track of the previous interval’s end value as prevEnd, initially set to the end value of the first interval.

Hint 4
We then iterate from the second interval. If the current interval doesn't overlap, we update prevEnd to the current interval's end and continue. Otherwise, we set prevEnd to the minimum of prevEnd and the current interval’s end, greedily removing the interval that ends last to retain as many intervals as possible.
'''