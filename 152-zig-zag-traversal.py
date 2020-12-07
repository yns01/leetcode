from typing import List
from collections import deque


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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def recurse(node, level):
            if not node:
                return

            if level >= len(self.result):
                self.result.append(deque())
            if level % 2 == 0:
                self.result[level].append(node.val)
            else:
                self.result[level].appendleft(node.val)

            recurse(node.left, level+1)
            recurse(node.right, level+1)

            return

        self.result = []
        recurse(root, 0)

        return self.result

    def zigzagLevelOrderBFS(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return

        que, level, result = deque(), deque(), []
        que.append(root)
        zig = True

        while que:
            for _ in range(len(que)):
                n = que.popleft()
                if zig:
                    level.append(n.val)
                else:
                    level.appendleft(n.val)

                if n.left:
                    que.append(n.left)
                if n.right:
                    que.append(n.right)

            result.append(level)
            level = deque()
            zig = zig ^ 1

        return result


tree = TreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right.insert_left(60)
right.insert_right(80)
print(Solution().zigzagLevelOrder(tree))
print(Solution().zigzagLevelOrderBFS(tree))
