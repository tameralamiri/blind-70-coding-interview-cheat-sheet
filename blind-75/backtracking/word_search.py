'''
Word Search
Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:



Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: true
Example 2:



Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"

Output: false
Constraints:

1 <= board.length, board[i].length <= 5
1 <= word.length <= 10
board and word consists of only lowercase and uppercase English letters.

Recommended Time & Space Complexity
You should aim for a solution with O(m * (4^n)) time and O(n) space, where m is the number of cells in the given board and n is the size of the given word.

Hint 1
As we can start at any cell on the board, we can explore all paths from that cell. Can you think of an algorithm to do so? Also, you should consider a way to avoid visiting a cell that has already been visited in the current path.

Hint 2
We can use a hash set to avoid revisiting a cell in the current path by inserting the (row, col) of the visiting cell into the hash set and exploring all paths (four directions, as we can move to four neighboring cells) from that cell. Can you think of the base condition for this recursive path? Maybe you should consider the board boundaries, and also, we can extend a path if the character at the cell matches the character in the word.

Hint 3
We can use backtracking, starting from each cell on the board with coordinates (row, col) and index i for the given word. We return false if (row, col) is out of bounds or if board[row][col] != word[i]. When i reaches the end of the word, we return true, indicating a valid path. At each step, we add (row, col) to a hash set to avoid revisiting cells. After exploring the four possible directions, we backtrack and remove (row, col) from the hash set.
'''