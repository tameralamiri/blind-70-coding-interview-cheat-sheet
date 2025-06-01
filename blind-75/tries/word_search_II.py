'''
Word Search II
Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:



Input:
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
],
words = ["bat","cat","back","backend","stack"]

Output: ["cat","back","backend"]
Example 2:



Input:
board = [
  ["x","o"],
  ["x","o"]
],
words = ["xoxo"]

Output: []
Constraints:

1 <= board.length, board[i].length <= 10
board[i] consists only of lowercase English letter.
1 <= words.length <= 100
1 <= words[i].length <= 10
words[i] consists only of lowercase English letters.
All strings within words are distinct.


Recommended Time & Space Complexity
You should aim for a solution with O(m * n * 4 * (3^(t-1)) + s) time and O(s) space, where m is the number of rows, n is the number of columns, t is the maximum length of any word and s is the sum of the lengths of all the words.

Hint 1
To search for a word in the grid, we can use backtracking by starting at each cell, simultaneously iterating through the word and matching the characters with the cells, recursively visiting the neighboring cells. However, if we are given a list of words and need to search for each one, it becomes inefficient to iterate through each word and run backtracking for each. Can you think of a better way? Perhaps a data structure could help with more efficient word search and insertion.

Hint 2
We can use a Trie to efficiently search for multiple words. After inserting all words into the Trie, we traverse the grid once. For each character in the grid, we check if it exists in the current Trie node. If not, we prune the search. If we encounter an "end of word" flag in the Trie node, we know a valid word has been found. But how can we add that word to the result list? Maybe you should think about what additional information you can store in the Trie node.

Hint 3
When we insert a word into the Trie, we can store the word's index. Why? Because when we want to add the word to the result list after finding a valid word, we can easily add it using the index. After adding that word, we put index = -1 as we shouldn't add the word multiple times to the result list. How can you implement this?

Hint 4
We insert all the words into the Trie with their indices marked. Then, we iterate through each cell in the grid. At each cell, we start at the root of the Trie and explore all possible paths. As we traverse, we match characters in the cell with those in the Trie nodes. If we encounter the end of a word, we take the index at that node and add the corresponding word to the result list. Afterward, we unmark that index and continue exploring further paths.
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        