// Last updated: 02/03/2026, 13:59:44
#include <vector>

class Solution {
public:
    int chalkReplacer(std::vector<int>& chalk, int k) {
        // Step 1: Calculate the total chalk usage in one complete round
        long long total_chalk = 0;
        for (int ch : chalk) {
            total_chalk += ch;
        }
        
        // Step 2: Reduce k by the total chalk usage in complete rounds
        k %= total_chalk;
        
        // Step 3: Identify the student who will replace the chalk
        for (int i = 0; i < chalk.size(); ++i) {
            if (k < chalk[i]) {
                return i;
            }
            k -= chalk[i];
        }
        
        // This line should theoretically never be reached due to the problem constraints
        return -1;
    }
};
