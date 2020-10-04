class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if not root:
            return None

        candidate, current = None, root

        while current:
            if current is p:
                current = current.right
            elif p.val <= current.val:
                candidate = current
                current = current.left
            elif p.val > current.val:
                current = current.right

        return candidate


n = TreeNode(2)
n.right = TreeNode(2)

a = Solution().inorderSuccessor(n, n)
print(n.right is a)
