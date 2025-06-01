'''
Merge Intervals
Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

You may return the answer in any order.

Note: Intervals are non-overlapping if they have no common point. For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

Example 1:

Input: intervals = [[1,3],[1,5],[6,7]]

Output: [[1,5],[6,7]]
Example 2:

Input: intervals = [[1,2],[2,3]]

Output: [[1,3]]
Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= start <= end <= 1000

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(nlogn) time and O(n) space, where n is the size of the input array.

Hint 1
Sorting the given intervals in ascending order based on their start values is beneficial, as it helps in identifying overlapping intervals efficiently. How can you determine if two intervals overlap?

Hint 2
If two intervals are sorted in ascending order by their start values, they overlap if the start value of the second interval is less than or equal to the end value of the first interval.

Hint 3
We iterate through the sorted intervals from left to right, starting with the first interval in the output list. From the second interval onward, we compare each interval with the last appended interval. Can you determine the possible cases for this comparison?

Hint 4
The two cases are: if the current interval overlaps with the last appended interval, we update its end value to the maximum of both intervals' end values and continue. Otherwise, we append the current interval and proceed.

'''