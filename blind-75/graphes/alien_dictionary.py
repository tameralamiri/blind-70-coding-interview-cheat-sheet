'''
Alien Dictionary
There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
There is no index i such that a[i] != b[i] and a.length < b.length.
Example 1:

Input: ["z","o"]

Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".

Example 2:

Input: ["hrn","hrf","er","enn","rfnn"]

Output: "hernf"
Explanation:

from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know get 'r' < 'n'
from "enn" and "rfnn" we know 'e'<'r'
so one possibile solution is "hernf"
Constraints:

The input words will contain characters only from lowercase 'a' to 'z'.
1 <= words.length <= 100
1 <= words[i].length <= 100

Recommended Time & Space Complexity
You should aim for a solution with O(N + V + E) time and O(V + E) space, where N is the sum of the lengths of all the strings, V is the number of unique characters (vertices), and E is the number of edges.

Hint 1
Can you think of this as a graph problem? Characters from a through z are nodes. What could the edges represent here? How can you create edges from the given words? Perhaps you should try comparing two adjacent words.


Hint 2
The relative ordering of the characters can be treated as edges. For example, consider the words ordered as ["ape", "apple"]. "ape" comes before "apple", which indicates that 'e' is a predecessor of 'p'. Therefore, there is a directed edge e -> p, and this dependency should be valid across all the words. In this way, we can build an adjacency list by comparing adjacent words. Can you think of an algorithm that is suitable to find a valid ordering?

Hint 3
We can use Topological Sort to ensure every node appears after its predecessor. Using DFS, we traverse the graph built from the adjacency list. A visited map tracks nodes in the current DFS path: False means not in the path, and True means in the path. If any DFS call returns True, it indicates a cycle and we return immediately. How do we extract the ordering from this DFS?

Hint 4
When we visit a node and its children and don't find a cycle, we mark the node as False in the map and append it to the result, treating this as a post-order traversal. If we find a cycle, we return an empty string; otherwise, we return the result list.
'''
from typing import List
class Solution:
    def foreign_dictionary(self, words: List[str]) -> str:
        pass