class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def recurse(node: TreeNode):
            if not node:
                return 0

            ls = recurse(node.left)
            rs = recurse(node.right)

            self.result += abs(ls - rs)
            return ls + rs + node.val

        if not root:
            return 0

        self.result = 0
        recurse(root)
        return self.result


three = TreeNode(3)
five = TreeNode(5)
sven = TreeNode(7)
two = TreeNode(2, three, five)
nin = TreeNode(9, None, sven)
root = TreeNode(4, two, nin)

print(Solution().findTilt(root))
