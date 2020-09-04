from typing import List
import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(node: TreeNode):
    if not node:
        return None

    nodes = queue.Queue()
    nodes.put(node)

    while not nodes.empty():
        n = nodes.get()
        print(n.val)
        nodes.put(n.left) if n.left else None
        nodes.put(n.right) if n.right else None

    return None


class Solution:
    def __init__(self):
        self.preorder_index = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        inorder_map = {}
        for i, n_val in enumerate(inorder):
            inorder_map[n_val] = i

        return self._build(preorder, self.preorder_index, inorder_map, 0, len(preorder)-1)

    def _build(self, preorder, preorder_index, inorder_map, inorder_left, inorder_right):
        if inorder_left > inorder_right:
            return None

        if preorder_index >= len(preorder):
            return None

        n = TreeNode(preorder[preorder_index])
        self.preorder_index += 1

        n.left = self._build(preorder, self.preorder_index,
                             inorder_map, inorder_left, inorder_map[n.val]-1)

        n.right = self._build(preorder, self.preorder_index,
                              inorder_map, inorder_map[n.val]+1, inorder_right)

        return n


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

level_order_traversal(Solution().buildTree(preorder, inorder))
