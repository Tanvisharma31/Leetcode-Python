# Last updated: 5/5/2026, 1:19:47 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
9        if not head or not head.next or k == 0:
10            return head
11
12        # Step 1: find length and tail
13        n = 1
14        tail = head
15        while tail.next:
16            tail = tail.next
17            n += 1
18
19        # Step 2: reduce k
20        k %= n
21        if k == 0:
22            return head
23
24        # Step 3: make circular
25        tail.next = head
26
27        # Step 4: find new tail
28        steps = n - k
29        new_tail = head
30        for _ in range(steps - 1):
31            new_tail = new_tail.next
32
33        # Step 5: break
34        new_head = new_tail.next
35        new_tail.next = None
36
37        return new_head