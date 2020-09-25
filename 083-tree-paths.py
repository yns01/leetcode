from typing import List


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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def recurse(root: TreeNode):
            if not root:
                return

            path.append(str(root.val))

            recurse(root.left)
            recurse(root.right)

            if not root.left and not root.right:
                res.append('->'.join(path))

            path.pop()

        res, path = [], []
        recurse(root)
        return res


tree = TreeNode(50)
left = tree.insert_left(30)
# right = tree.insert_right(70)

ll = left.insert_left(10)
lr = left.insert_right(40)
rl = lr.insert_left(60)
rr = lr.insert_right(80)


print(Solution().binaryTreePaths(tree))
