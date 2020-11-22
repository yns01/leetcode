from collections import defaultdict, deque
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


# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        lb, rb = 0, 0
        que = deque()
        que.append((root, 0, 0))
        groups = defaultdict(list)

        while que:
            n, row, col = que.popleft()
            # If add the row and values to be able to sort based on their row then value
            groups[col].append((row, n.val))
            lb = min(lb, col)
            rb = max(rb, col)

            if n.left:
                que.append((n.left, row + 1, col - 1))

            if n.right:
                que.append((n.right, row + 1, col + 1))

        result = []
        for i in range(lb, rb+1):
            nodes = sorted(groups[i])
            result.append([n[1] for n in nodes])

        return result


tree = TreeNode(10)
left = tree.insert_left(4)
right = tree.insert_right(3)

ll = left.insert_left(11)
lr = left.insert_right(8)
rr = right.insert_right(13)
rl = right.insert_left(5)

#Expected:  [[11], [4], [10, 5, 8], [3], [13]]
# Nodes 10, 5 and 8 are sorted first on their row then their values
print(Solution().verticalTraversal(tree))
