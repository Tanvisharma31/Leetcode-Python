# Last updated: 02/03/2026, 14:03:11
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for w in strs:
            s=''.join(sorted(w))
            d[s].append(w)
        return list(d.values())