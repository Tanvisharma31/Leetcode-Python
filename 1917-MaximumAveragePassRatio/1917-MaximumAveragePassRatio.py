# Last updated: 02/03/2026, 13:59:49
import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        classes = [(num / denom - (num + 1) / (denom + 1), num, denom) for num, denom in classes]
        heapq.heapify(classes)
        if classes[0][0] == 0: return 1
        for _ in range(extraStudents):
            _, num, denom = heappop(classes)
            heappush(classes, ((num + 1) / (denom + 1) - (num + 2) / (denom + 2), num + 1, denom + 1))
        return sum(num / denom for _, num, denom in classes) / len(classes)