class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        def recurse(node):
            if not node:
                return (0, 0)

            left_sum, left_count = recurse(node.left)
            right_sum, right_count = recurse(node.right)

            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            current_avg = current_sum / current_count

            self.res = max(self.res, current_avg)

            return (current_sum, current_count)

        if not root:
            return 0.0

        self.res = 0.0
        recurse(root)
        return self.res


root = TreeNode(5, TreeNode(6), TreeNode(1))
print(Solution().maximumAverageSubtree(root))
