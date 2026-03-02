# Last updated: 02/03/2026, 13:56:49
class Solution:
  def kthCharacter(self, k: int) -> str:
    return string.ascii_lowercase[(k - 1).bit_count()]