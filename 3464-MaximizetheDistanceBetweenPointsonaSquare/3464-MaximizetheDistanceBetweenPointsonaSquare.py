# Last updated: 25/04/2026, 16:49:54
1class Solution:
2    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
3        res = []
4        for x, y in points:
5            if x == 0:
6                res.append(y)
7            elif y == side:
8                res.append(side + x)
9            elif x == side:
10                res.append(side * 3 - y)
11            else:
12                res.append(side * 4 - x)
13        res.sort()
14        def check(n : int) -> bool:
15            idx = [0] * k
16            curr = res[0]
17            for i in range(1, k):
18                j = bisect_left(res, curr + n)
19                if j == len(res):
20                    return False
21                idx[i] = j
22                curr = res[j]
23            if curr - res[0] <= side * 4 - n:
24                return True
25            
26            for idx[0] in range(1, idx[1]):
27                for j in range(1, k):
28                    while res[idx[j]] < res[idx[j - 1]] + n:
29                        idx[j] += 1
30                        if idx[j] == len(res):
31                            return False
32                if res[idx[-1]] - res[idx[0]] <= side * 4 - n:
33                    return True
34            return False
35        
36        left, right = 1, side + 1
37        while left + 1 < right:
38            mid = (left + right) // 2
39            if check(mid):
40                left = mid
41            else:
42                right = mid
43        return left