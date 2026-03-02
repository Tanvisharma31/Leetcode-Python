// Last updated: 02/03/2026, 13:57:12
class Solution {
public:
    int minimumPushes(string word) {
        // Step 1: Count frequency of each letter
        unordered_map<char, int> freq;
        for (char c : word) {
            freq[c]++;
        }
        
        // Step 2: Extract frequencies and sort in descending order
        vector<int> frequencies;
        for (const auto& pair : freq) {
            frequencies.push_back(pair.second);
        }
        sort(frequencies.rbegin(), frequencies.rend()); // Sort in descending order
        
        // Step 3: Calculate the minimum number of pushes
        int total_cost = 0;
        vector<int> push_counts = {1, 1, 1, 1, 1, 1, 1, 1, 2}; // Costs for keys 2-9
        
        int n = frequencies.size();
        for (int i = 0; i < n; ++i) {
            int key_index = i % 8; // Key index for current letter (0-based index for 8 keys)
            int presses = (i / 8) + 1; // Each key can have multiple presses
            total_cost += frequencies[i] * presses;
        }
        
        return total_cost;
    }
};
