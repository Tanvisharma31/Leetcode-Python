// Last updated: 02/03/2026, 14:01:18
class Solution {
 public:
  int minAddToMakeValid(string s) {
    int l = 0;
    int r = 0;

    for (const char c : s)
      if (c == '(') {
        ++l;
      } else {
        if (l == 0)
          ++r;
        else
          --l;
      }

    return l + r;
  }
};