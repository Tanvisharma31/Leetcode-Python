# Last updated: 02/03/2026, 14:03:20
class Solution:
    def reverse(self, x: int) -> int:
        sign= 1 if x>0 else -1
        x=abs(x)
        res=0
        while x:
            d=x%10
            res=res*10+d
            x=x//10
        if (res*sign)>(2**31-1) or (res*sign)<(-2**31-1) :
            return 0
        else:
            return res*sign