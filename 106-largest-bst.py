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
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def recurse(node: TreeNode):
            if not node:
                return (True, +math.inf, -math.inf, 0)

            l_bst, l_min, l_max, lc = recurse(node.left)

            r_bst, r_min, r_max, rc = recurse(node.right)

            if l_bst and r_bst and l_max < node.val <= r_min:
                self.largest_bst = max(self.largest_bst, lc + rc + 1)

                return (True, min(l_min, node.val), max(r_max, node.val), lc + rc + 1)
            else:
                return (False, 0, 0, 0)

        self.largest_bst = -math.inf
        recurse(root)

        return self.largest_bst if self.largest_bst != -math.inf else 0


tree = TreeNode(4)
left = tree.insert_left(1)
right = tree.insert_right(6)
# left.insert_left(1)
# left.insert_right(40)
rl = right.insert_left(5).insert_left(2)


print(Solution().largestBSTSubtree(tree))
