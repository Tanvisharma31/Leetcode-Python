# Last updated: 02/03/2026, 13:56:26
class Solution:
    def answerString(self, word: str, fri: int) -> str:
        if fri == 1:
            return word
        n = len(word)
        req = n-fri+1
        ans = "" 
        ind = []
        maxval = max(list(word))
        for i in range(n):
            if word[i] == maxval:
                ans = max(ans,word[i:i+req])

             
        return ans
        