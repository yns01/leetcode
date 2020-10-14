# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node, current_depth):
            if not node:
                return (None, current_depth)

            current_depth += 1
            left_subtree, left_depth = dfs(node.left, current_depth)
            right_subtree, right_depth = dfs(node.right, current_depth)

            if not left_subtree and not right_subtree:
                return (node, current_depth)

            if left_depth > right_depth:
                return (left_subtree, left_depth)
            elif right_depth > left_depth:
                return (right_subtree, right_depth)
            else:
                return (node, right_depth)

        if not root:
            return none

        return dfs(root, -1)[0]
