# Last updated: 02/03/2026, 13:55:43
import math

class Solution:
    def minimumK(self, nums: List[int]) -> int:
        s=sum(nums)
        n=len(nums)
        s_k=max(1,math.ceil(s**(1/3)),math.ceil(n**0.5))
        k=s_k
        while True:
            l=k*k
            op=0
            for x in nums:
                op+=(x+k-1)//k
                if op>l:
                    break
            if op<=l:
                return k
            k+=1