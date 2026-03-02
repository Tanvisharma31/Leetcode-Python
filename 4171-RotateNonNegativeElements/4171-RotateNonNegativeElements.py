# Last updated: 02/03/2026, 13:55:44
from typing import List

class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        n=[x for x in nums if x>=0]
        if not n:
            return nums
        m=len(n)
        eff=k%m
        r=n[eff:]+n[:eff]
        res=[]
        r_i=0
        for num in nums:
            if num<0:
                res.append(num)
            else:
                res.append(r[r_i])
                r_i+=1
        return res