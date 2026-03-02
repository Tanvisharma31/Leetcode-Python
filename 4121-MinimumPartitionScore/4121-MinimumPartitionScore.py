# Last updated: 02/03/2026, 13:55:50
import sys
sys.setrecursionlimit(2000)
class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n=len(nums)
        p=[0]*(n+1)
        for i in range(n):
            p[i+1]=p[i]+nums[i]
        def val(s):
            return s*(s+1)//2
        def cost(m,i):
            s=p[i]-p[m]
            return val(s)
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            dp[i]=cost(0,i)
        for st in range(2,k+1):
            new_dp=[float('inf')]*(n+1)
            def s(left,right,o1,o2):
                if left>right:
                    return
                mid=(left+right)//2
                be=-1
                m_v=float('inf')
                s_s=max(o1,st-1)
                e_s=min(o2,mid-1)
                for p1 in range(s_s,e_s+1):
                    c_v=dp[p1]+cost(p1,mid)
                    if c_v<m_v:
                        m_v=c_v
                        be=p1
                new_dp[mid]=m_v
                s(left,mid-1,o1,be)
                s(mid+1,right,be,o2)
            s(st,n,st-1,n-1)
            dp=new_dp
        return dp[n]