// Last updated: 02/03/2026, 13:58:40
class Solution {
 public:
  bool isCircularSentence(string sentence) {
    for (int i = 0; i < sentence.length(); ++i)
      if (sentence[i] == ' ' && sentence[i - 1] != sentence[i + 1])
        return false;
    return sentence.front() == sentence.back();
  }
};