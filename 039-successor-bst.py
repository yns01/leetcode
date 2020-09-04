class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if not root:
            return None

        stack, current = [], root

        while current:
            stack.append(current)
            if current is p:
                current = current.right
            elif p.val < current.val:
                current = current.left
            elif p.val > current.val:
                current = current.right

        while stack:
            n = stack.pop()
            if n.val > p.val:
                return n

        return None


n = TreeNode(2)
n.right = TreeNode(3)

Solution().inorderSuccessor(n, n)
