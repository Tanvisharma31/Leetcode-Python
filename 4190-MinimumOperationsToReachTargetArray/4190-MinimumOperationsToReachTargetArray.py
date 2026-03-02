# Last updated: 02/03/2026, 13:55:35
class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        v_f=set()
        for n_val,t_val in zip(nums,target):
            if n_val!=t_val:
                v_f.add(n_val)
        return len(v_f)