# Last updated: 02/03/2026, 13:59:52
class Solution:
    #ab
    #pqrs
    
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1),len(word2))
        
        res = ""
        for i in range(min_len):
            res += word1[i]
            res += word2[i]
            
        if min_len == len(word1):
            res += word2[min_len:len(word2)]
        else:
            res += word1[min_len:len(word1)]
        return res