# Last updated: 12/03/2026, 14:09:20
class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        
        parents = list(range(n))

        def find(i):            
            i2 = i
            while parents[i] != i:
                i = parents[i]
            if parents[i2] != i:
                parents[i2] = i
            return i

        def union(p1, p2):
            parents[p2] = p1

        count = n

        heap = []
        min_w = inf
        for s,t,w,m in edges:
            if m:
                if w < min_w:
                    min_w = w
                p1 = find(s)
                p2 = find(t)
                if p1 != p2:
                    count -= 1
                    union(p1,p2)
                else:
                    return -1
            else:
                heapq.heappush(heap,(-w, s, t))

        if count == 1:
            return min_w

        #print(min_w)

        heap2 = []
        while heap:
            w, s, t = heapq.heappop(heap)

            p1 = find(s)
            p2 = find(t)
            if p1 == p2:
                continue
            else:
                count -= 1
                union(p1,p2)

            #print(w,s,t, heap2, k)
            if k > 0:
                heapq.heappush(heap2, w)
                k -= 1
                w = -w * 2
            else:
                w = min(-w * 2, - heappushpop(heap2, w))
            #print(w)
            if w < min_w:
                min_w = w

            if count == 1:
                return min_w

        return -1


            
            