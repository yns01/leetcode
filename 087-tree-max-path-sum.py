import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert_left(self, value):
        self.left = TreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = TreeNode(value)
        return self.right


class Solution:
    def __init__(self):
        self.max_sum = -math.inf

    def maxPathSum(self, root: TreeNode) -> int:
        def recurse(node: TreeNode) -> int:
            if not node:
                return 0

            left_sum = recurse(node.left)
            right_sum = recurse(node.right)

            left_path = left_sum + node.val
            right_path = right_sum + node.val
            left_right_path = left_sum + right_sum + node.val
            self.max_sum = max(self.max_sum,
                               left_path,
                               right_path,
                               left_right_path,
                               node.val)

            # For the recursion, we can only pick one path,
            # left, right, or stop at the current node.
            # We can't include left and right, as it would not be
            # a valid path from the root of the tree.
            return max(left_path, right_path, node.val)

        recurse(root)

        return self.max_sum


tree = TreeNode(-10)
left = tree.insert_left(9)
right = tree.insert_right(20)

# ll = left.insert_left(3)
# lr = left.insert_right(-7)

# ll.insert_left(-10)
# ll.insert_right(4)

right.insert_left(15)
right.insert_right(7)
print(Solution().maxPathSum(tree))
