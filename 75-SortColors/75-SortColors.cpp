// Last updated: 02/03/2026, 14:03:02
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int left = 0; // Pointer to the leftmost boundary of elements equal to 0
        int right = nums.size() - 1; // Pointer to the rightmost boundary of elements equal to 2
        int curr = 0; // Pointer to traverse the array
        
        // Iterate until the current pointer crosses the right pointer
        while (curr <= right) {
            // If the current element is 0, swap it with the element at the left boundary and move both pointers to the right
            if (nums[curr] == 0) {
                swap(nums[left], nums[curr]);
                left++;
                curr++;
            }
            // If the current element is 2, swap it with the element at the right boundary and move the right pointer to the left
            else if (nums[curr] == 2) {
                swap(nums[right], nums[curr]);
                right--;
            }
            // If the current element is 1, move the current pointer to the right
            else {
                curr++;
            }
        }
    }
};
