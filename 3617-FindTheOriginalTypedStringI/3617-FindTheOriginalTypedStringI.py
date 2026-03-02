# Last updated: 02/03/2026, 13:56:43
class Solution:
  def possibleStringCount(self, word: str) -> int:
    return 1 + sum(a == b
                   for a, b in itertools.pairwise(word))