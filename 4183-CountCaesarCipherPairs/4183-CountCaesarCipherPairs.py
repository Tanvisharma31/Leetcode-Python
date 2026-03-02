# Last updated: 02/03/2026, 13:55:39
from collections import defaultdict
class Solution:
    def countPairs(self, words: List[str]) -> int:
        f=defaultdict(int)
        ans=0
        for w in words:
            base=ord(w[0])
            signature=tuple((ord(c)-base)%26 for c in w)
            ans+=f[signature]
            f[signature]+=1
        return ans