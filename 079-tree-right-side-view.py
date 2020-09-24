from typing import List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        return self.traversal(root)

    def traversal(self, node: TreeNode):
        if not node:
            return []

        nodes = collections.deque()
        nodes.append(node)

        right_view = []
        while nodes:
            for i in range(len(nodes)):
                n = nodes.popleft()
                if i == 0:
                    right_view.append(n.val)

                if n.right:
                    nodes.append(n.right)

                if n.left:
                    nodes.append(n.left)

        return right_view
