# Last updated: 02/03/2026, 13:55:28
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=[]
        for w in words:
            t=0
            for c in w:
                i=ord(c)-ord('a')
                t+=weights[i]
            r=t%26
            t_c=25-r
            m=chr(ord('a')+t_c)
            res.append(m)
        return "".join(res)