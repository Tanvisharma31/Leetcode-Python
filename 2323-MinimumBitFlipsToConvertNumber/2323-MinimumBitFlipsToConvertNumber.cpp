// Last updated: 02/03/2026, 13:59:05
class Solution {
 public:
  int minBitFlips(unsigned start, unsigned goal) {
    return popcount(start ^ goal);
  }
};