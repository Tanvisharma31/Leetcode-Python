// Last updated: 02/03/2026, 14:02:29
class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        long miss = 1;  // The smallest number that cannot be formed
        int i = 0;
        int patches = 0;
        
        while (miss <= n) {
            if (i < nums.size() && nums[i] <= miss) {
                miss += nums[i];
                i++;
            } else {
                miss += miss;
                patches++;
            }
        }
        
        return patches;
    }
};