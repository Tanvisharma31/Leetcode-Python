# Last updated: 02/03/2026, 13:55:46
from collections import Counter
class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        p=[word[:k] for word in words if len(word)>=k]
        p_c=Counter(p)
        g=0
        for c in p_c.values():
            if c >=2:
                g+=1
        return g
        