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
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if root.val == key:
            if not root.left and not root.right:
                root = None
            elif root.right:
                successor = self.successor(root)
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)
            else:
                predecessor = self.predecessor(root)
                root.val = predecessor.val
                root.left = self.deleteNode(root.left, predecessor.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root

    def successor(self, node: TreeNode):
        current = node.right
        successor = None
        while current:
            successor = current
            current = current.left

        return successor

    def predecessor(self, node: TreeNode):
        current = node.left
        predecessor = None
        while current:
            predecessor = current
            current = current.right

        return predecessor


tree = TreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right.insert_left(60).insert_left(59).insert_left(58)
right.insert_right(80)
