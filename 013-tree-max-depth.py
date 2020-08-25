class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1


root = TreeNode(0)
root.left = TreeNode(5)
root.right = TreeNode(5)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(5)
root.right.right.right.right.left = TreeNode(5)
root.left.left = TreeNode(5)
root.left.left.left = TreeNode(5)


print(Solution().maxDepth(root))
