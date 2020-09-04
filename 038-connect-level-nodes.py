from collections import deque


class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return None

        current = root
        q = deque()
        q.append(current)

        while len(q):
            prev = None
            for _ in range(len(q)):
                n = q.popleft()

                if prev:
                    prev.next = n

                prev = n

                if n.left:
                    q.append(n.left)

                if n.right:
                    q.append(n.right)

        return root


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)

root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

Solution().connect(root)
print(root)
