// Last updated: 02/03/2026, 13:58:53
#include <vector>
#include <algorithm>

class Solution {
public:
    // Method to find the length of the longest subarray consisting of the maximum element.
    int longestSubarray(std::vector<int>& nums) {
        // Get the maximum value in the array.
        int maxValue = *std::max_element(nums.begin(), nums.end());
        // Initialize answer (longest subarray length) and counter for current subarray length.
        int longestSubarrayLength = 0, currentSubarrayLength = 0;
      
        // Iterate over each element in the array.
        for (int value : nums) {
            // Check if the current element equals the maximum value.
            if (value == maxValue) {
                // Increment the current subarray length as it is part of a subarray containing max elements.
                ++currentSubarrayLength;
                // Update the answer with the maximum subarray length found so far.
                longestSubarrayLength = std::max(longestSubarrayLength, currentSubarrayLength);
            } else {
                // Reset current subarray length if the current element is not the maximum value.
                currentSubarrayLength = 0;
            }
        }
        // Return the length of the longest subarray found.
        return longestSubarrayLength;
    }
};
