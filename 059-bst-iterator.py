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
        self.last_element_popped = None

        self.__populate_stack()

    def next(self) -> int:
        e = self.stack.pop()
        self.last_element_popped = e
        self.__populate_stack()

        return e.val

    def hasNext(self) -> bool:
        if self.stack:
            return True

        self.__populate_stack()
        return self.stack

    def __populate_stack(self):
        node = self.last_element_popped.right if self.last_element_popped else self.root

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
