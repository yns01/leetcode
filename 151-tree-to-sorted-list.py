class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def increasingBST(self, root: TreeNode) -> TreeNode:
        def recurse(node: TreeNode):
            if not node:
                return

            recurse(node.left)
            if self.prev:
                self.prev.right = node
            else:
                self.head = node

            self.prev = node
            node.left = None
            recurse(node.right)
            return None

        self.prev = None
        self.head = None
        recurse(root)

        return self.head
