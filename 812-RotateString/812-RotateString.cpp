// Last updated: 02/03/2026, 14:01:38
class Solution {
 public:
  bool rotateString(string s, string goal) {
    return s.length() == goal.length() && (s + s).find(goal) != string::npos;
  }
};