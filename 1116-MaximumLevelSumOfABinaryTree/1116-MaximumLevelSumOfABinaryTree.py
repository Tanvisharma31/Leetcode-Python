# Last updated: 02/03/2026, 14:01:03
class Solution:
    def maxLevelSum(self, r: Optional[TreeNode]) -> int:
        z = Counter()
        (f:=lambda n,i:n and (z.update({i:n.val}),f(n.left,i+1),f(n.right,i+1)))(r,1)
        return max(z,key=z.get)