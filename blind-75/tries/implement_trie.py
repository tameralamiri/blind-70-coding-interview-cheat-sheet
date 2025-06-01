'''
Implement Trie (Prefix Tree)
A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.

Implement the PrefixTree class:

PrefixTree() Initializes the prefix tree object.
void insert(String word) Inserts the string word into the prefix tree.
boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
Example 1:

Input: 
["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]

Output:
[null, null, true, false, true, null, true]

Explanation:
PrefixTree prefixTree = new PrefixTree();
prefixTree.insert("dog");
prefixTree.search("dog");    // return true
prefixTree.search("do");     // return false
prefixTree.startsWith("do"); // return true
prefixTree.insert("do");
prefixTree.search("do");     // return true
Constraints:

1 <= word.length, prefix.length <= 1000
word and prefix are made up of lowercase English letters.


Recommended Time & Space Complexity
You should aim for a solution with O(n) time for each function call and O(t) space, where n is the length of the given string and t is the total number of nodes created in the Trie.

Hint 1
A Trie is structured as a tree-like data structure where each node contains a hash map (or an array for fixed character sets) to store references to its child nodes, which represent characters. Each node also includes a boolean flag to indicate whether the current node marks the end of a valid word. The Trie starts with a root node that does not hold any character and serves as the entry point for all operations. The child nodes of the root and subsequent nodes represent unique characters from the words stored in the Trie, forming a hierarchical structure based on the prefixes of the words.

Hint 2
To insert a word, we iterate through the characters of the word with index i, starting at the root of the Trie as the current node. If the current node already contains word[i], we continue to the next character and move to the node that word[i] points to. If word[i] is not present, we create a new node for word[i] and continue the process until we reach the end of the word. We mark the boolean variable as true as it is the end of the inserted word.

Hint 3
Searching for a word is similar to inserting, but instead of creating new nodes, we return false if we don't find a character in the path while iterating or if the end-of-word marker is not set to true when we reach the end of the word.
'''

class PrefixTree:

    def __init__(self):
        

    def insert(self, word: str) -> None:


    def search(self, word: str) -> bool:
        

    def startsWith(self, prefix: str) -> bool:
        
        