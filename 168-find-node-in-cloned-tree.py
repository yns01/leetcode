class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def insert_left(self, value):
        self.left = TreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = TreeNode(value)
        return self.right


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def recurse(p, q):
            if not p or not q:
                return None

            if p is target:
                return q

            return recurse(p.left, q.left) or recurse(p.right, q.right)

        return recurse(original, cloned)


root = TreeNode(7)
l = root.insert_left(4)
r = root.insert_right(3)

r.insert_left(6)
r.insert_right(19)


root1 = TreeNode(7)
l1 = root1.insert_left(4)
r1 = root1.insert_right(3)

r1.insert_left(6)
r1.insert_right(19)

print(Solution().getTargetCopy(root, root1, r).val)
