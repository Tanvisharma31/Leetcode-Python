# Last updated: 01/04/2026, 20:45:04
1class Solution:
2    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
3        
4        def move_from_left_to_right():
5            nonlocal current_sum
6            element = left_set.pop()
7            current_sum -= element 
8            right_set.add(element)
9
10        def move_from_right_to_left():
11            nonlocal current_sum
12            element = right_set.pop(0)
13            left_set.add(element)
14            current_sum += element 
15
16        k -= 1
17
18        current_sum = sum(nums[:dist + 2])
19        left_set = SortedList(nums[1:dist + 2])
20        right_set = SortedList()
21
22        while len(left_set) > k:
23            move_from_left_to_right()
24
25        min_cost = current_sum 
26
27        for i in range(dist + 2, len(nums)):
28            outgoing_element = nums[i - dist - 1]
29            if outgoing_element in left_set:
30                left_set.remove(outgoing_element)
31                current_sum -= outgoing_element
32            else:
33                right_set.remove(outgoing_element)
34
35            incoming_element = nums[i]
36            if left_set and incoming_element < left_set[-1]:
37                left_set.add(incoming_element)
38                current_sum += incoming_element
39            else:
40                right_set.add(incoming_element)
41
42            while len(left_set) < k:
43                move_from_right_to_left()
44            while len(left_set) > k:
45                move_from_left_to_right()
46
47            min_cost = min(min_cost, current_sum)
48
49        return min_cost 