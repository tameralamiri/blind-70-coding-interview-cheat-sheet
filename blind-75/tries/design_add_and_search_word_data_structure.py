'''
Design Add and Search Word Data Structure
Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:

void addWord(word) Adds word to the data structure.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
Example 1:

Input:
["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]

Output:
[null, null, null, null, false, true, true, true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true
Constraints:

1 <= word.length <= 20
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters

Recommended Time & Space Complexity
You should aim for a solution with O(n) time for each function call and O(t + n) space, where n is the length of the string and t is the total number of nodes created in the Trie.

Hint 1
A brute force solution would be to store each added word in a list and search linearly through the list for a word every time. This would be an O(m * n) solution, where m is the size of the list and n is the length of the string. Can you think of a better way? Maybe there is a tree-like data structure.

Hint 2
We can use a Trie to implement adding and searching for words efficiently. Adding a word follows the standard Trie insertion process. However, when searching for a word containing '.', which can match any character, we need a different approach. Instead of directly matching, we consider all possible characters at the position of '.' and recursively check the rest of the word for each possibility. How would you implement it?

Hint 3
We traverse the word with index i, starting at the root of the Trie. For normal characters, we search as usual. When encountering a dot ('.'), we try all possible characters by recursively extending the search in each direction. If any path leads to a valid word, we return true; otherwise, we return false. Although we try all paths for a dot, the time complexity is still O(n) because there are at most two dots ('.') in the word, making the complexity O((26^2) * n).

'''
class WordDictionary:

    def __init__(self):
        

    def addWord(self, word: str) -> None:
        

    def search(self, word: str) -> bool:
        
