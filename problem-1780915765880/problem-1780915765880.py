# Last updated: 6/8/2026, 4:19:25 PM
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        x=[]
        y=[]
        z=[]
        for i in nums:
            if i<pivot:
                x.append(i)
            elif i==pivot:
                y.append(i)
            else:
                z.append(i)
        return x+y+z

        