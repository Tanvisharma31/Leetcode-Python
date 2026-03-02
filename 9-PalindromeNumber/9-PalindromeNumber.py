# Last updated: 02/03/2026, 14:03:19
class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=str(x)
        if n==n[::-1]:
            return True
        else:
            return False