# Last updated: 02/03/2026, 13:55:36
class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        a=0
        for _ in range(k):
            for i in range(65):
                c=math.comb(i,k-1)
                if n<=c:
                    a|=(1<<i)
                    k-=1
                    break
                else:
                    n-=c
        return a