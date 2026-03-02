# Last updated: 02/03/2026, 14:00:18
class Solution:
  def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    words = sentence.split()

    for i, word in enumerate(words):
      if word.startswith(searchWord):
        return i + 1

    return -1