class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert_left(self, value):
        self.left = Node(value)
        return self.left

    def insert_right(self, value):
        self.right = Node(value)
        return self.right


class Solution:
    def __init__(self):
        self.prev = None
        self.head = None

    def treeToDoublyList(self, root: Node) -> Node:
        if not root:
            return

        def recurse(node: Node):
            if not node:
                return None

            recurse(node.left)
            if self.prev:
                self.prev.right = node
            else:
                self.head = node

            node.left = self.prev
            self.prev = node

            recurse(node.right)

            return

        recurse(root)
        self.prev.right = self.head
        self.head.left = self.prev

        return self.head

    def v2(self, root: Node) -> Node:
        if not root:
            return

        stack = []
        current = root
        prev, head = None, None

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                if prev:
                    prev.right = current
                    current.left = prev
                else:
                    head = current

                prev = current
                current = current.right

        prev.right = head
        head.left = prev

        return head


tree = Node(50)
# left = tree.insert_left(30)
right = tree.insert_right(70)
# left.insert_left(10)
# left.insert_right(40)
# right.insert_left(60)
right.insert_right(80)

r = Solution().treeToDoublyList(tree)
print(r)
