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
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def recurse(node: TreeNode, running_sum: int):
            if not node:
                return

            path.append(node.val)
            running_sum += node.val

            recurse(node.left, running_sum)
            recurse(node.right, running_sum)

            if not node.left and not node.right and running_sum == sum:
                res.append(path[:])

            path.pop()

        path, res = [], []
        recurse(root, 0)
        return res


tree = TreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(-50)

ll = left.insert_left(10)
lr = left.insert_right(40)
rl = lr.insert_left(60)
rr = lr.insert_right(80)

right.insert_right(90)

print(Solution().pathSum(tree, 90))
