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
        self.max_d = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def diameter(root: TreeNode):
            if not root:
                return 0

            left_d = diameter(root.left)
            right_d = diameter(root.right)

            self.max_d = max(self.max_d, left_d+right_d)

            return max(left_d, right_d) + 1

        diameter(root)
        return self.max_d


tree = TreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)

ll = left.insert_left(10)
lr = left.insert_right(40)
rl = lr.insert_left(60)
rr = lr.insert_right(80)

ll.insert_left(0).insert_left(12)
rl.insert_left(23)

print(Solution().diameterOfBinaryTree(tree))
