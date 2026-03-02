# Last updated: 02/03/2026, 13:55:33
class Solution:
    def countMonobit(self, n: int) -> int:
        if n<0:
            return 0
        c=1
        num=1
        while True:
            can=(1<<num)-1
            if can>n:
                break
            c+=1
            num+=1
        return c