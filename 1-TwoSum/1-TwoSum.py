# Last updated: 5/27/2026, 6:27:22 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1 = 0
        ptr2 = len(numbers)-1
        while True:
            total = numbers[ptr1]+numbers[ptr2]
            if total>target:
                ptr2-=1
            elif total==target:
                return [ptr1+1, ptr2+1]
            else:
                ptr1+=1

        return -1