class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def insert_left(self, value):
        self.left = TreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = TreeNode(value)
        return self.right


class Solution:
    def lowestCommonAncestor(self, p: TreeNode, q: TreeNode) -> TreeNode:
        def build_path(start: TreeNode, path):
            if not start:
                return

            path[start] = start.parent
            build_path(start.parent, path)

        def compare_path(start: TreeNode, path):
            if not start:
                return None

            if start in path:
                return start

            return compare_path(start.parent, path)

        p_path = {}
        build_path(p, p_path)
        return compare_path(q, p_path)

    def lowestCommonAncestorv1(self, p: TreeNode, q: TreeNode) -> TreeNode:
        p_depth, q_depth = self.depth(p), self.depth(q)

        while p_depth > q_depth:
            p_depth -= 1
            p = p.parent

        while q_depth > p_depth:
            q_depth -= 1
            q = q.parent

        while p != q:
            p = p.parent
            q = q.parent

        return p

    def depth(self, node):
        if not node:
            return 0

        return self.depth(node.parent) + 1


tree = TreeNode(3)
left = tree.insert_left(5)
right = tree.insert_right(1)

ll = left.insert_left(6)
lr = left.insert_right(2)
rr = right.insert_right(0)
rl = right.insert_left(8)

lrl = lr.insert_left(7)
lrr = lr.insert_right(4)

nonTreeNode = TreeNode(99)

print(Solution().lowestCommonAncestor(lrr, nonTreeNode))
print(Solution().lowestCommonAncestorv1(lrr, nonTreeNode))
