from typing import List
import queue


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

        qe = queue.Queue()
        qe.put((root, 0))

        traversal = []
        while not qe.empty():
            node, level = qe.get()
            if len(traversal) <= level:
                traversal.append([node.val])
            else:
                traversal[level].append(node.val)

            if node.left:
                qe.put((node.left, level+1))

            if node.right:
                qe.put((node.right, level+1))

        return traversal


tree = TreeNode(50)
left = tree.insert_left(40)
left_left = left.insert_left(30)
left_left_left = left_left.insert_left(20)
left_left_left.insert_left(10)
result = Solution().levelOrder(tree)
print(result)
