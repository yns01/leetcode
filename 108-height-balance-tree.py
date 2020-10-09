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
    def isBalanced(self, root: TreeNode) -> bool:
        def is_balanced(root):
            if not root:
                return (True, -1)

            ib, left_height = is_balanced(root.left)
            if not ib:
                return (False, 0)

            ib, right_height = is_balanced(root.right)
            if not ib:
                return (False, 0)

            return (abs(left_height - right_height) <= 1, max(left_height, right_height) + 1)

        return is_balanced(root)[0]

    def isBalanced2(self, root: TreeNode) -> bool:
        if not root:
            return True

        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        if not root:
            return -1

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return max(left_height, right_height) + 1
