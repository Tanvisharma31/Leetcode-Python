# Last updated: 02/03/2026, 14:01:10
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def min_rot(target: int) -> int:
            to_top = to_bottom = 0
            for x, y in zip(tops, bottoms):
                if x != target and y != target:
                    return inf
                if x != target:
                    to_top += 1  # 把 y 旋转到上半
                elif y != target:
                    to_bottom += 1  # 把 x 旋转到下半
            return min(to_top, to_bottom)

        ans = min(min_rot(tops[0]), min_rot(bottoms[0]))
        return -1 if ans == inf else ans
