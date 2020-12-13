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


def level_order_traversal(node: TreeNode):
    if not node:
        return None

    nodes = deque()
    nodes.append(node)

    while nodes:
        for _ in range(len(nodes)):
            n = nodes.popleft()
            print(str(n.val) + '->', end='')

            nodes.append(n.left) if n.left else None
            nodes.append(n.right) if n.right else None

        print('')

    return None


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        nodes = []
        self.tree_to_sorted_list(root, nodes)
        return self.sorted_list_to_bst(nodes, 0, len(nodes) - 1)

    def tree_to_sorted_list(self, root, nodes):
        if not root:
            return

        self.tree_to_sorted_list(root.left, nodes)
        nodes.append(root)
        self.tree_to_sorted_list(root.right, nodes)

    def sorted_list_to_bst(self, nodes, left, right):
        if not nodes or left > right:
            return None

        mid = (right - left) // 2 + left
        root = nodes[mid]

        root.left = self.sorted_list_to_bst(nodes, left, mid - 1)
        root.right = self.sorted_list_to_bst(nodes, mid + 1, right)

        return root


root = TreeNode(1, None, TreeNode(2, None, TreeNode(
    3, None, TreeNode(4, None, TreeNode(5)))))


level_order_traversal(Solution().balanceBST(root))
