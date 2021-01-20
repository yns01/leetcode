class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        def recurse(node):
            if not node:
                return (0, 0)

            left_sum, left_count = recurse(node.left)
            right_sum, right_count = recurse(node.right)

            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            current_avg = current_sum / current_count

            self.res = max(self.res, current_avg)

            return (current_sum, current_count)

        if not root:
            return 0.0

        self.res = 0.0
        recurse(root)
        return self.res

    # Variation: return true if a node's value is the average of all its children
    def average_equals(self, root: TreeNode) -> bool:
        def recurse(node):
            if not node:
                return (False, 0, 0)

            found, ls, lc = recurse(node.left)
            if found:
                return (True, 0, 0)

            found, rs, rc = recurse(node.right)
            if found:
                return (True, 0, 0)

            # We consider that a single node without children does not equals the average of its
            # non existent children. Otherwise, a root node with value 0, without children
            # would return true.

            children_sum, children_count, children_avg = ls + rs, lc + rc, None
            if children_count != 0:
                children_avg = children_sum / children_count

            if children_avg is not None and node.val == children_avg:
                return (True, 0, 0)

            current_sum = ls + rs + node.val
            current_count = lc + rc + 1

            return (False, current_sum, current_count)

        if not root:
            return False

        return recurse(root)[0]


root = TreeNode(5, TreeNode(6), TreeNode(1))
print(Solution().maximumAverageSubtree(root))

root = TreeNode(3, TreeNode(1, TreeNode(4)), TreeNode(4))
print(Solution().average_equals(root))
