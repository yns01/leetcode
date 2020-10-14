# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/class Solution:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node: TreeNode, min_v, max_v):
            if not node:
                return (min_v, max_v)

            if node.val < min_v:
                min_v = node.val

            elif node.val > max_v:
                max_v = node.val

            left_min, left_max = dfs(node.left, min_v, max_v)
            right_min, right_max = dfs(node.right, min_v, max_v)

            if left_max - left_min > right_max - right_min:
                return (left_min, left_max)
            else:
                return (right_min, right_max)

        min_f, max_f = dfs(root, root.val, root.val)
        return max_f - min_f
