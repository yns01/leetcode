from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = TreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = TreeNode(value)
        return self.right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None

        p_ancestors = self.find_node(root, p)
        q_ancestors = self.find_node(root, q)

        lca = root
        while p_ancestors and q_ancestors:
            pa, qa = p_ancestors.popleft(), q_ancestors.popleft()
            if pa is qa:
                lca = pa
            else:
                break

        return lca

    def find_node(self, root: TreeNode, target: TreeNode) -> deque:
        ancestors = deque()

        def recurse(node: TreeNode):
            if not node:
                return False

            ancestors.append(node)

            if node is target:
                return True

            found = recurse(node.left)
            if found:
                return found

            found = recurse(node.right)
            if found:
                return found

            ancestors.pop()
            return found

        recurse(root)

        return ancestors


tree = TreeNode(3)
left = tree.insert_left(5)
right = tree.insert_right(1)

ll = left.insert_left(6)
lr = left.insert_right(2)
rr = right.insert_right(0)
rl = right.insert_left(8)

lrl = lr.insert_left(7)
lrr = lr.insert_right(4)


print(Solution().lowestCommonAncestor(tree, lrl, lrr).val)
