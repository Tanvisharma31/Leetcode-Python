# Last updated: 6/14/2026, 7:20:20 PM
1from collections import deque
2
3
4# Definition for singly-linked list.
5# class ListNode:
6#     def __init__(self, val=0, next=None):
7#         self.val = val
8#         self.next = next
9class Solution:
10    def pairSum(self, head: Optional[ListNode]) -> int:
11        container = deque()
12
13        iterNode = head
14
15        while iterNode is not None:
16            container.append(iterNode.val)
17            iterNode = iterNode.next
18
19        result = 0
20
21        while container:
22            front = container.popleft()
23            back = container.pop()
24            result = max(result, front + back)
25
26        return result