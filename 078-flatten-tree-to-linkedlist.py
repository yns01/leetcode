from typing import List
from collections import deque


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
        self.left_rightmost = None

    def flatten(self, root: TreeNode) -> None:
        if not root:
            return

        left_most = self.flatten(root.left)
        right_most = self.flatten(root.right)

        if not root.left and not root.right:
            return root

        if root.left and root.right:
            left_most.right = root.right
            root.right = root.left
            root.left = None
            return right_most

        if not root.left:
            return right_most

        root.right = root.left
        root.left = None
        return left_most


tree = TreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right.insert_left(60)
right.insert_right(80)

s = Solution()
print(s.flatten(tree))
# s.flatten(tree)
# print(s.flatten(tree))
