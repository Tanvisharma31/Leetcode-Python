// Last updated: 02/03/2026, 13:59:28
class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        // Check if it's possible to create the 2D array
        if (original.size() != m * n) {
            return {};  // Return an empty array if the size doesn't match
        }

        // Initialize the 2D array
        vector<vector<int>> result(m, vector<int>(n));

        // Fill the 2D array with elements from the original array
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                result[i][j] = original[i * n + j];
            }
        }

        return result;
    }
};
