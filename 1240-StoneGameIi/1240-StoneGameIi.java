// Last updated: 02/03/2026, 14:00:57
class Solution {
    // s will hold the prefix sum of the piles array
    private int[] prefixSum;
    // f is a memoization table where f[i][m] will store the result of dfs(i, m)
    private Integer[][] memo;
    // n is the total number of piles
    private int n;

    public int stoneGameII(int[] piles) {
        n = piles.length;
        prefixSum = new int[n + 1];
        memo = new Integer[n][n + 1];
        // Calculate prefix sums for the piles array for easy range sum queries
        for (int i = 0; i < n; ++i) {
            prefixSum[i + 1] = prefixSum[i] + piles[i];
        }
        // Start the game with the first pile (index 0) and initial 'M' value of 1
        return dfs(0, 1);
    }

    private int dfs(int i, int m) {
        // If the next player can take all remaining piles, return the sum of those piles
        if (m * 2 >= n - i) {
            return prefixSum[n] - prefixSum[i];
        }
        // If we have already computed this state, return the stored value
        if (memo[i][m] != null) {
            return memo[i][m];
        }
        int result = 0;
        // Try all possible x moves from the current position
        for (int x = 1; x <= m * 2; ++x) {
            // Choose the move that maximizes the current player's score
            result = Math.max(result, prefixSum[n] - prefixSum[i] - dfs(i + x, Math.max(m, x)));
        }
        // Store the result in the memoization table before returning
        memo[i][m] = result;
        return result;
    }
}
