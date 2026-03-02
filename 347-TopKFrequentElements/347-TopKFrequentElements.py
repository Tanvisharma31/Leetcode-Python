# Last updated: 02/03/2026, 14:02:22
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        for n in nums:
            d[n]+=1
        return sorted(d,key=d.get,reverse=True)[:k]