# Last updated: 05/04/2026, 15:36:02
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U')==moves.count('D') and moves.count('L')==moves.count('R')