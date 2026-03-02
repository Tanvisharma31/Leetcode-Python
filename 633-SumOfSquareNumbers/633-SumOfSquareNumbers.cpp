// Last updated: 02/03/2026, 14:02:01
class Solution {
public:
    bool judgeSquareSum(int c) {
        if (c < 0) return false;
        
        long low = 0;
        long high = (long) sqrt(c);
        
        while (low <= high) {
            long sum = low * low + high * high;
            if (sum == c)
                return true;
            else if (sum < c)
                low++;
            else
                high--;
        }
        
        return false;
    }
};
