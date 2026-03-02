// Last updated: 02/03/2026, 14:00:15
import java.util.PriorityQueue;

class Solution {
    public int rangeSum(int[] nums, int n, int left, int right) {
        final int MOD = 1000000007;
        
        // Create a priority queue (min-heap) to store subarray sums
        PriorityQueue<Long> minHeap = new PriorityQueue<>();
        long[] prefixSum = new long[n + 1];
        
        // Calculate prefix sums
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }
        
        // Generate all subarray sums and store them in the heap
        for (int start = 0; start < n; start++) {
            for (int end = start + 1; end <= n; end++) {
                minHeap.offer(prefixSum[end] - prefixSum[start]);
            }
        }
        
        // Extract and sum the elements from the heap in the range [left, right]
        long result = 0;
        int count = 0;
        
        while (!minHeap.isEmpty()) {
            long sum = minHeap.poll();
            count++;
            if (count >= left && count <= right) {
                result = (result + sum) % MOD;
            }
            if (count > right) break;
        }
        
        return (int) result;
    }
}
