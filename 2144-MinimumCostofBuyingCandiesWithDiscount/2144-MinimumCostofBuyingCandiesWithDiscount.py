# Last updated: 6/1/2026, 8:06:21 AM
1class Solution:
2    def minimumCost(self, cost: List[int]) -> int:
3        total_cost = 0
4        cost.sort(reverse=True)
5
6        l = len(cost)
7
8        num_three = l // 3
9        mod_three = l % 3
10
11        pos = 0
12        for i in range(0, num_three):
13            first_candy = cost[pos]
14            total_cost = total_cost + first_candy
15            pos+=1
16            second_candy = cost[pos]
17            total_cost = total_cost + second_candy 
18            pos+=2
19            # third candy is free
20
21        for i in range(0, mod_three):
22            candy = cost[pos]
23            total_cost = total_cost + candy
24            pos+=1
25
26        return total_cost
27            
28        