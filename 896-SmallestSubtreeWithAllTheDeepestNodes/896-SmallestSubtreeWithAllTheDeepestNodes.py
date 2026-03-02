# Last updated: 02/03/2026, 14:01:26
class Solution:
    def subtreeWithAllDeepest(self, root):
        def dfs(node):
            if not node:
                return (None, 0)   # (lca, depth)

            left_lca, left_depth = dfs(node.left)
            right_lca, right_depth = dfs(node.right)

            if left_depth > right_depth:
                return (left_lca, left_depth + 1)
            if left_depth < right_depth:
                return (right_lca, right_depth + 1)

            # depths equal → current node is LCA
            return (node, left_depth + 1)

        return dfs(root)[0]

