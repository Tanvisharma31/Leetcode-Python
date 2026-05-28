# Last updated: 5/28/2026, 2:39:21 PM
1class TrieNode:
2    __slots__ = ['children', 'bestLen', 'bestIdx']
3    
4    def __init__(self):
5        self.children = {}
6        self.bestLen = float('inf')
7        self.bestIdx = float('inf')
8
9class Solution:
10    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
11        root = TrieNode()
12        
13        for i, word in enumerate(wordsContainer):
14            n = len(word)
15            curr = root
16            
17            if n < curr.bestLen or (n == curr.bestLen and i < curr.bestIdx):
18                curr.bestLen = n
19                curr.bestIdx = i
20                
21            for char in reversed(word):
22                if char not in curr.children:
23                    curr.children[char] = TrieNode()
24                
25                curr = curr.children[char]
26                
27                if n < curr.bestLen or (n == curr.bestLen and i < curr.bestIdx):
28                    curr.bestLen = n
29                    curr.bestIdx = i
30                    
31        ans = []
32        
33        for query in wordsQuery:
34            curr = root
35            
36            for char in reversed(query):
37                if char not in curr.children:
38                    break
39                curr = curr.children[char]
40            
41            ans.append(curr.bestIdx)
42            
43        return ans