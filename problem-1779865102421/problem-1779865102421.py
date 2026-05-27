# Last updated: 5/27/2026, 12:28:22 PM
class Solution:
    def numberOfSpecialChars(self, word: str, ans = 0) -> int:
        
        for ch, CH in zip(ascii_lowercase, ascii_uppercase):

            if ch not in word or CH not in word: continue
  
            ans+= word.rfind(ch) < word.find(CH)

        return ans