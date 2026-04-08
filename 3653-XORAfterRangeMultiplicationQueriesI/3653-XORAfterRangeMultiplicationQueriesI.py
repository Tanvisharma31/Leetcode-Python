# Last updated: 08/04/2026, 19:19:12
1import numpy as np
2class Solution:
3    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
4        # Convert nums to an int64 array to prevent overflow during multiplication
5        # before the modulo operation.
6        arr = np.array(nums, dtype=np.int64)
7        MOD = 10**9 + 7
8
9        for li, ri, ki, vi in queries:
10            # Create a slice from li to ri (inclusive) with step ki
11            # In NumPy, the stop index is exclusive, so we use ri + 1
12            arr[li : ri + 1 : ki] = (arr[li : ri + 1 : ki] * vi) % MOD
13
14        # Perform a bitwise XOR reduction across the entire array
15        # np.bitwise_xor.reduce is the vectorized way to XOR all elements
16        return int(np.bitwise_xor.reduce(arr))