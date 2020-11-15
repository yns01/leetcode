class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = TreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = TreeNode(value)
        return self.right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recurse(node: TreeNode):
            if not node:
                return None

            left = recurse(node.left)
            right = recurse(node.right)

            if node is p or node is q:
                self.found_count += 1
                return node

            if left and right:
                return node

            return left or right

        self.found_count = 0
        lca = recurse(root)
        return lca if self.found_count == 2 else None


tree = TreeNode(3)
left = tree.insert_left(5)
right = tree.insert_right(1)

ll = left.insert_left(6)
lr = left.insert_right(2)
rr = right.insert_right(0)
rl = right.insert_left(8)

lrl = lr.insert_left(7)
lrr = lr.insert_right(4)

nonTreeNode = TreeNode(99)

print(Solution().lowestCommonAncestor(tree, lrl, lrr).val)
print(Solution().lowestCommonAncestor(tree, lrl, nonTreeNode))
