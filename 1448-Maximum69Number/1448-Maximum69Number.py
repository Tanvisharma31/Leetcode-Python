# Last updated: 02/03/2026, 14:00:36

class Solution:
  def maximum69Number(self, num: int) -> int:
    return int(str(num).replace('6', '9', 1))