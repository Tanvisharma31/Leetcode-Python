# Last updated: 5/12/2026, 12:36:53 PM
class Solution:
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        need = 0
        for actual, minimum in reversed(tasks):
            need = max(minimum, need + actual)
        return need
