# Last updated: 22/04/2026, 16:59:46
1class Solution:
2    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
3        def _get_distance(s1,s2):
4            cnt = 0
5            for i in range(len(s1)):
6                if s1[i]!=s2[i]:
7                    cnt+=1
8                if cnt==3:
9                    return False
10            return True
11
12        good = []
13        for query in queries:
14            for d in dictionary:
15                dist = _get_distance(query,d)
16                if dist:
17                    good.append(query)
18                    break
19        return good