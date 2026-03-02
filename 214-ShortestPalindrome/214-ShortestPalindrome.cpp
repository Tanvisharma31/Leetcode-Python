// Last updated: 02/03/2026, 14:02:45
class Solution {
 public:
  string shortestPalindrome(string s) {
    const string t = {s.rbegin(), s.rend()};
    const string_view sv_s(s);
    const string_view sv_t(t);

    for (int i = 0; i < s.length(); ++i)
      if (sv_s.substr(0, s.length() - i) == sv_t.substr(i))
        return t.substr(0, i) + s;

    return t + s;
  }
};