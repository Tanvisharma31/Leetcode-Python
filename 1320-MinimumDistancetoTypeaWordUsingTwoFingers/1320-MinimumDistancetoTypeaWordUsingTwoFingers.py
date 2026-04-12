# Last updated: 12/04/2026, 15:04:45
diff = ord('A')
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
distance_lookup = {}
for c1 in alphabet:
    for c2 in alphabet:
        x1, x2 = (ord(c1) - ord('A')) % 6, (ord(c2) - ord('A')) % 6
        y1, y2 = (ord(c1) - ord('A')) // 6, (ord(c2) - ord('A')) // 6
        distance_lookup[(c1, c2)] = abs(x1 - x2) + abs(y1 - y2)


class Solution:
    def minimumDistance(self, word: str) -> int:
        # well my first impression approach was O(2**n), so that won't work. 
        # oh I can do this dijkstra-style with length as the key. Probably not actually, because the core difficulty is likely that something that's more expensive now might be less expensive later. Trying it out just-in-case because I'm struggling to think of a test-case to prove it unusable. Oh duh, because I'm always evaluating the overall cheapest possible option, this should in fact work -- I'm not going to the end the fastest, I'm getting the cheapest path to the end. 
        # can't key by length, because I have to be able to go try a different key-combo in the past that was more expensive at the time but might be cheaper overall. Still not sure what test case i need for that, but this is leetcode, I don't *need* to be sure.

        # looking at my score there's probably a log(n) answer somewhere. Probably keep a heap of some kind for the costs of each finger. Going to try cleaning up my dijkstra first. Somehow that got slower, actually. Actually it has to be better than logn, either that or dijkstra's just really slow for this class of problem, because dijkstra is logn already.

        # if I iterate linearly, I'm asking at each step: what's the cheapest amongst all previous steps of (key1 to current key, key2 to previous key) or (key1 to previous key, key2 to current key)

        # eh, I don't have time for this. Looking at the top ans.
        # yeah, dp. It's a linear solution, though obviously heavily linear based on the runtimes.
        # They're making an array of infinities for every character at every point along n. Except for the first character in word, those are all zero. 
        # For each character in the word:
        # - dpi refers to the alphabet lookup at the current index and dpi1 refers to the previous one
        # - dist1 refers to the distance between the current character (val) and the last character (old)
        # - for each c1 in the alphabet
        # - - dist2 refers to the distance between c1 and val
        # - - dpi[c1] = min(dpi[c1], dpi1[c1] + dist1) referencing itself for the obvious reason of a previous iteration of the loop modifying it in the [old] value. Otherwise take the best cost to get to c1 anywhere plus the best cost old to val. Oh, that's because we're saying "what if we don't move one finger off of c1", and move the other to get to the val. This is the cost of leaving a finger on c1. We have to move the other finger off of [old] and onto [val] with dist1. We do this for each one because we're calculating "what's it cost to leave a finger there"
        # - - dpi[old] = min(dpi[old], dpi1[c1] + dist2) dpi[old] is again obvious. This is the cost of leaving a finger on the last character, and instead moving the other finger from WHEREVER it was left, which is why it's done for each character. It's the cost from c1 (wherever that finger was) to here (dist2). 
        # So in effect, dp[i] is the cost to get *a* finger there, no matter what character it is, but with the constraint given by the word meaning we always know one finger had to be on [old].

        n = len(word)

        dp = [0] * 26
        for c1, c2 in pairwise(word):
            c1_to_c2 = distance_lookup[(c1, c2)]
            new_dp = [inf] * 26
            for c in alphabet:
                c_to_c2 = distance_lookup[(c, c2)]
                ci = ord(c) - diff

                leave_on_c = c1_to_c2 + dp[ci]
                if leave_on_c < new_dp[ci]:
                    new_dp[ci] = leave_on_c
                
                leave_on_c1 = c_to_c2 + dp[ci]
                if leave_on_c1 < new_dp[ord(c1) - diff]:
                    new_dp[ord(c1) - diff] = leave_on_c1
            dp, new_dp = new_dp, dp
            new_dp.clear()
        
        return min(dp)
