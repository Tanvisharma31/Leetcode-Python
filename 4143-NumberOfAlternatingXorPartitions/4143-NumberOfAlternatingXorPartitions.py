# Last updated: 02/03/2026, 13:55:45
import collections
class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        MOD=10**9+7
        nt0=collections.defaultdict(int)
        nt1=collections.defaultdict(int)
        nt1[0]=1
        c_xor=0
        t1=0
        t2=0
        for x in nums:
            c_xor^=x
            t1=nt1[c_xor^target1]
            t2=nt0[c_xor^target2]
            nt0[c_xor]=(nt0[c_xor]+t1)%MOD
            nt1[c_xor]=(nt1[c_xor]+t2)%MOD
        return (t1+t2)%MOD