# Last updated: 02/03/2026, 14:02:06
from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len_s1, len_s2 = len(s1), len(s2)

        # If s1 is longer than s2, no permutation of s1 can be a substring of s2
        if len_s1 > len_s2:
            return False
        
        # Count the frequency of each character in s1
        s1_count = Counter(s1)
        window_count = Counter()  # Initialize the sliding window counter
        
        for i in range(len_s2):
            # Add the current character in the sliding window
            window_count[s2[i]] += 1
            
            # Once the window size exceeds s1's length, remove the character
            # that is no longer in the window (i.e., slide the window)
            if i >= len_s1:
                if window_count[s2[i - len_s1]] == 1:
                    del window_count[s2[i - len_s1]]  # Remove it if count becomes 0
                else:
                    window_count[s2[i - len_s1]] -= 1
            
            # Compare the two frequency counters
            if window_count == s1_count:
                return True
        
        # No permutation of s1 found in s2
        return False
