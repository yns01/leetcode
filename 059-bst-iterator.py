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


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []
        self.__populate_stack(self.root)

    def next(self) -> int:
        e = self.stack.pop()
        if e.right:
            self.__populate_stack(e.right)

        return e.val

    def hasNext(self) -> bool:
        return len(self.stack) >= 1

    def __populate_stack(self, from_node: TreeNode):
        node = from_node

        while node:
            self.stack.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
tree = TreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right.insert_left(60)
right.insert_right(80)


obj = BSTIterator(tree)
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
# param_1 = obj.next()
# param_2 = obj.hasNext()
