# Last updated: 5/26/2026, 11:34:16 AM
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seen = set()
        counted = set()
        count = 0

        for letter in word:
            other = letter.swapcase()
            if other in seen and letter.lower() not in counted:
                count += 1
                counted.add(letter.lower())
            seen.add(letter)
        return count