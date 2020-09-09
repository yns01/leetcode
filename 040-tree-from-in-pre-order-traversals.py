from typing import List, Dict
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

        in_order_map = {}
        for i, n in enumerate(inorder):
            in_order_map[n] = i

        return self.__build_tree(preorder, in_order_map, 0, len(inorder)-1)

    def __build_tree(self, preorder: List[int], in_order_map: Dict[int, int], in_order_elements_start: int, in_order_elements_end: int):
        if self.preorder_index >= len(preorder):
            return None

        if in_order_elements_start > in_order_elements_end:
            return None

        n = TreeNode(preorder[self.preorder_index])
        self.preorder_index += 1

        n.left = self.__build_tree(
            preorder, in_order_map, in_order_elements_start, in_order_map[n.val]-1)

        n.right = self.__build_tree(
            preorder, in_order_map, in_order_map[n.val]+1, in_order_elements_end)

        return n


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

level_order_traversal(Solution().buildTree(preorder, inorder))
