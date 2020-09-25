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
        if not root:
            return None

        if min(p.val, q.val) < root.val < max(p.val, q.val):
            return root
        elif root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


tree = TreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)
ll = left.insert_left(10)
lr = left.insert_right(40)
# right.insert_left(60)
# right.insert_right(80)

print(Solution().lowestCommonAncestor(tree, ll, lr).val)
