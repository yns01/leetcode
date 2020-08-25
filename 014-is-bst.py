import unittest


class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


class Solution:
    def isValidBST(self, root: BinaryTreeNode) -> bool:
        # return _is_bst(root, None, None)
        return self._is_bst_2(root)

    def _is_bst_2(self, node: BinaryTreeNode):
        if not node:
            return True

        prev, current, stack = None, node, []

        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                if prev and not prev.val < current.val:
                    return False

                prev = current
                current = current.right

        return True

    def _is_bst(self, node: BinaryTreeNode, left_boundary: int, right_boundary: int) -> bool:
        if not node:
            return True

        is_bst = self._is_bst(node.left, left_boundary, node.val)
        if not is_bst:
            return False

        if left_boundary != None and not left_boundary < node.val:
            return False

        if right_boundary != None and not node.val < right_boundary:
            return False

        return self._is_bst(node.right, node.val, right_boundary)


class Test(unittest.TestCase):

    def test_valid_full_tree(self):
        tree = BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        result = Solution().isValidBST(tree)
        self.assertTrue(result)

    def test_both_subtrees_valid(self):
        tree = BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(60)
        right.insert_left(70)
        right.insert_right(90)
        result = Solution().isValidBST(tree)
        self.assertFalse(result)

    def test_descending_linked_list(self):
        tree = BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        result = Solution().isValidBST(tree)
        self.assertTrue(result)

    def test_out_of_order_linked_list(self):
        tree = BinaryTreeNode(50)
        right = tree.insert_right(70)
        right_right = right.insert_right(60)
        right_right.insert_right(80)
        result = Solution().isValidBST(tree)
        self.assertFalse(result)

    def test_one_node_tree(self):
        tree = BinaryTreeNode(50)
        result = Solution().isValidBST(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)
