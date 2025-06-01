'''
Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.

Example 1:

Input: s = "neetcode", wordDict = ["neet","code"]

Output: true
Explanation: Return true because "neetcode" can be split into "neet" and "code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen","ape"]

Output: true
Explanation: Return true because "applepenapple" can be split into "apple", "pen" and "apple". Notice that we can reuse words and also not use all the words.

Example 3:

Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]

Output: false
Constraints:

1 <= s.length <= 200
1 <= wordDict.length <= 100
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n * m * t) time and O(n) space, where n is the length of the string s, m is the number of words in wordDict, and t is the maximum length of any word in wordDict.

Hint 1
Try to think of this problem in terms of recursion, where we explore all possibilities. We iterate through the given string s, attempting to pick a word from wordDict that matches a portion of s, and then recursively continue processing the remaining string. Can you determine the recurrence relation and base condition?

Hint 2
The base condition is to return true if we reach the end of the string s. At each recursive call with index i iterating through s, we check all words in wordDict and recursively process the remaining string by incrementing i by the length of the matched word. If any recursive path returns true, we immediately return true. However, this solution is exponential. Can you think of an optimization? Maybe you should consider an approach that avoids repeated work.

Hint 3
We can avoid recalculating results for recursive calls by using memoization. Since we iterate with index i, we can use a hash map or an array of the same length as s to cache the results of recursive calls and prevent redundant computations.
'''