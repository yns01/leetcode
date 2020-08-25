from typing import List
import queue
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        qe = deque()
        qe.append((root, 0))

        traversal = []
        while len(qe):
            node, level = qe.popleft()
            if len(traversal) <= level:
                traversal.append([node.val])
            else:
                traversal[level].append(node.val)

            if node.left:
                qe.append((node.left, level+1))

            if node.right:
                qe.append((node.right, level+1))

        return traversal

    def levelOrderv2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        qe, traversal = deque(), []
        qe.append(root)

        while len(qe):
            level_nodes = []

            for _ in range(len(qe)):
                node = qe.popleft()
                level_nodes.append(node.val)

                if node.left:
                    qe.append(node.left)

                if node.right:
                    qe.append(node.right)

            traversal.append(level_nodes)
        return traversal


tree = TreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right.insert_left(60)
right.insert_right(80)
result = Solution().levelOrderv2(tree)
print(result)
