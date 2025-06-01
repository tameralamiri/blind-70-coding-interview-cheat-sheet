'''
Find Median From Data Stream
The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

For example:

For arr = [1,2,3], the median is 2.
For arr = [1,2], the median is (1 + 2) / 2 = 1.5
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far.
Example 1:

Input:
["MedianFinder", "addNum", "1", "findMedian", "addNum", "3" "findMedian", "addNum", "2", "findMedian"]

Output:
[null, null, 1.0, null, 2.0, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.findMedian(); // return 1.0
medianFinder.addNum(3);    // arr = [1, 3]
medianFinder.findMedian(); // return 2.0
medianFinder.addNum(2);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:

-100,000 <= num <= 100,000
findMedian will only be called after adding at least one integer to the data structure.

Recommended Time & Space Complexity
You should aim for a solution with O(logn) time for addNum(), O(1) time for findMedian(), and O(n) space, where n is the current number of elements.

Hint 1
A naive solution would be to store the data stream in an array and sort it each time to find the median, resulting in O(nlogn) time for each findMedian() call. Can you think of a better way? Perhaps using a data structure that allows efficient insertion and retrieval of the median can make the solution more efficient.

Hint 2
If we divide the array into two parts, we can find the median in O(1) if the left half can efficiently return the maximum and the right half can efficiently return the minimum. These values determine the median. However, the process changes slightly if the total number of elements is odd — in that case, the median is the element from the half with the larger size. Can you think of a data structure which is suitable to implement this?

Hint 3
We can use a Heap (Max-Heap for the left half and Min-Heap for the right half). Instead of dividing the array, we store the elements in these heaps as they arrive in the data stream. But how can you maintain equal halves of elements in these two heaps? How do you implement this?

Hint 4
We initialize a Max-Heap and a Min-Heap. When adding an element, if the element is greater than the minimum element of the Min-Heap, we push it into the Min-Heap; otherwise, we push it into the Max-Heap. If the size difference between the two heaps becomes greater than one, we rebalance them by popping an element from the larger heap and pushing it into the smaller heap. This process ensures that the elements are evenly distributed between the two heaps, allowing us to retrieve the middle element or elements in O(1) time.

'''

class MedianFinder:

    def __init__(self):
        

    def addNum(self, num: int) -> None:
        

    def findMedian(self) -> float:
        
        