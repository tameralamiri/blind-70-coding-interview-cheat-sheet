

Problem:
Given laps like [["Harold 160", "Gina 140", "Juan 130"],["Harold 150", "Gina 146", "Juan 152"],["Harold 170", "Gina 141", "Juan 135"]] . Eliminate racer(s) per lap based on worst among the best (lowest) personal time.

[Harold, Gina, Juan]. It wasnt simple like worst time in each lap. It like you get eliminated if you have the worst personal time among the previous laps.
return a list of eliminated racers' names in order of their elimination. If racers are eliminated in the same lap, return them in alphabetical order.


You are given operations, an array containing the following two types of operations:
• [0, a, b] - Create and save a rectangle of size a x b ;
• [1, a, b] - Answer the question: "Could every one of the earlier saved rectangles fit in a box of size a x b". It is
possible to rotate rectangles by 90 degrees; ie: a rectangle of dimensions a x b can be rotated so that its dimensions
are b x a . Note: We're trying to fit each rectangle within the box separately (not all at the same time).
Your task is to return an array of booleans, representing the answers to the second type of operation, in the order they appear.
Note that the operations should be proceeded iteratively, so when operations [i] is executed only the results of the previous
operations o 1 1,..., i - 1 are available.
Example
• For operations = [[1, 1, 1]], the output should be solution (operations) = [true] .
There are no rectangles, so they all can be fit in any box.
• For operations = [[0, 1, 31], [O, 4, 21], [1, 3, 41], [1, 3, 2]] , the output should be
solution (operations) = [true, false]


Converting a list into a matrix by diagonally filling up the elements
mylist = [-2, -2, 1, 1, 4, 4, 3, 3, 3]
Desired Output:

res = [[3, 3, 4],
      [3, 4, 1],
      [1, -2, -2]]

Given an array consisting of 1s and 0s and an integer k find the number of sequences of size k in the array. Treat the array as circular meaning the last index of the array follows onto the first index.
Example:

array = [1,0,1,0,1,1], k = 4
solution_set = {1010, 0101}
result = 2

array = [1,0,1,0], k = 3
solution_set = {101, 010, 101(starting at 3rd index), 010(starting at 4th index}
result = 4


1. An easy question related to arrays. (easy)
2. A question involving strings & arrays. (easy)
3. A problem requiring array manipulations, such as reversing rows and columns rotating 90 degrees counterclockwise, and swapping rows and columns. (medium)
4. A string prefix matching problem, which could be solved using a trie. (medium)

Que1 -
Imagine that you are monitoring changes to user ratings for an online platform. Each user on this platform has an ID, a current rating (an integer between 1 and 2500), and a corresponding profile. The rating levels are based the following rules:

1 <= rating < 1000 = "beginner"
1000 <= rating < 1500 = "intermediate"
1500 <= rating < 2000 = "advanced"
2000 <= rating = "pro"
You are given an initial rating value and an array of integers changes representing changes to the rating. Your task is to calculate the final rating and return the level corresponding to that rating.

It is guaranteed that changes to the rating value will never result in it becoming less than 1 or greater than 2500.

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(changes.length^2) will fit within the execution time limit.

Ques2 -
You are given two arrays of integers a and b and an array queries containing the queries you are required to process. Every queries[i] can have one of the following two forms:

[0, i, x]. In this case, you need to add x to the current value of a[i].
[1, i, x]. In this case, you need to find the total number of pairs of indices j and j such that a[j] + b[j] = x.
Perform the given queries in order and return an array containing the results of the queries of the type [1, x].

Example:
For a = [1, 2, 3], b = [1, 4], and queries = [[1, 5], [0, 0, 2], [1, 5]], the output should be solution(a, b, queries). The arrays look like this initially:
a = [1, 2, 3]
b = [1, 4]

Ques3 -
Imagine that you are going fishing at the local pond. The size of the bait must be strictly smaller than the size of the fish for it to be of any use. However, each bait is removed from the pond and cannot be caught again. Each bait can be used up to 3 times before depletion.

Given two arrays of fish and baits, where fish[i] corresponds to the size of the ith fish in the pond, and baits[i] corresponds to the size of the jth bait, your task is to return the maximum number of fish you can catch from the pond with the given baits.

To compute the answer, you need to use each bait to its possible extent, going from the largest bait to the smallest bait. Use each bait to catch the largest fish remaining in the pond and move to the next bait if the current bait was used three times or if it is not strictly smaller than the largest remaining fish. When you run out of baits, return the number of caught fish.

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than
𝑂(max(fish.Length, baits.Length)3) will fit within the execution time limit.

Ques4 -
You are given an array of integers memory consisting of 0s and 1s—where the corresponding memory unit is free or not. memory[i] = 0 means that the ith memory unit is free, and memory[i] = 1 means it's occupied.

Your task is to perform two types of queries:

alloc x: Find the left-most memory block of x consecutive free memory units and mark these units as occupied (i.e., find the left-most contiguous subarray of 0s, and replace them all with 1s). If there are no blocks with x consecutive free units, return -1; otherwise return the index of the first position of the allocated block segment.

erase index: If there exists an allocated memory block starting at position index, free all its memory units. Otherwise, if the memory cell at position index was occupied before the very first operation ever applied to the memory, free this cell only. Return the length of the deleted memory block. If there is no allocated block starting at the position index, return

Given height of sticks in an array and the initial position of bird which has fixed stick height of 0, she picks up sticks from both side alternatively. In other words, it will first start right to find the stick and bring it to the initial position, then start left to do the same. Return all the indices from where the bird picks up the sticks until the total height of all sticks reaches 100.

Given a matrix of colors filled in the cells (or can be empty too), user takes turns to pop the cells. If the cell was empty, nothing happens but if user pops color filled cell, all the cells diagonally adjacent will also get popped if sharing the same color. So for eg:

4 3 2
1 0 2
0 1 1
1 4 4

is the matrix given and the user clicks on [2,1] then the following cells will pop:
[1,0], [2,1], [3,0]

If the cells pop, there's a simulation of all the colors above the cells popped to drop down. In the above example after popping the cells [[1,0], [2,1], [3,0] , cols 0 and 1 will be affected(all the cells above [1,0], [2,1], [3,0] will drop down):

0 0 2
0 0 2
0 3 1
4 4 4

will be the final state. As you observe color 4 from [0,0] fell down to [3,0]. Similarly for color 3 at 0,1. It's just like Candy Crush.

An array of slots is given which are all initially uncolored. n queries [x,y] will be given where x = position, y = color. Each query means to paint slot at x position with color y. For each query find out how many consecutive slot pairs share the same color.
Eg: [0,0,0,0,0,0]
Queries: [[1,2],[2,2],[0,3],[3,2],[1,1]]
Ans: [0, 1, 1, 2, 0]

Given a string (ex. “CodeSignal”) and n, replace the nth consonant to the next consonant. Probably LC medium.
Given an array of audiobooks listening time and a list of logs, return the index of the max value. (Don’t remember the detail)
Similar to LC3101, DP problem.