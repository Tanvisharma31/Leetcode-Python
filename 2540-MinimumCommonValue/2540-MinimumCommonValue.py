# Last updated: 5/19/2026, 2:52:20 PM
1from collections import deque
2
3class Solution:
4    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
5        # Cast the sorted arrays into double-ended queues
6        queue1 = deque(nums1)
7        queue2 = deque(nums2)
8        
9        # Erode the streams from the front until a match or exhaustion
10        while queue1 and queue2:
11            head1 = queue1[0]
12            head2 = queue2[0]
13            
14            if head1 == head2:
15                return head1  # First mutual element encountered is guaranteed the minimum
16            elif head1 < head2:
17                queue1.popleft()  # Erode the smaller value
18            else:
19                queue2.popleft()  # Erode the smaller value
20                
21        return -1