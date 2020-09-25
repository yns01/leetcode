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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def recurse(node: TreeNode, running_sum: int):
            if not node:
                return

            running_sum += node.val
            sum_found = recurse(node.left, running_sum)
            if sum_found:
                return True

            sum_found = recurse(node.right, running_sum)
            if sum_found:
                return True

            if not node.left and not node.right and running_sum == sum:
                return True

            return False

        # We use a local variable for the running_sum so when the recursion is back up,
        # it value is restored to what it was before the calls were made. It avoid substracting
        # when going back up the stack.
        # Also, we shortcut the recursion if we found the sum.
        return recurse(root, 0)


tree = TreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)

ll = left.insert_left(10)
lr = left.insert_right(40)
rl = lr.insert_left(60)
rr = lr.insert_right(80)

print(Solution().hasPathSum(tree, 90))
