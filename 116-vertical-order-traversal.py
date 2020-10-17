from typing import List
from collections import deque, defaultdict


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
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        node = root
        que = deque()
        que.append((node, 0))
        groups = defaultdict(list)
        min_col, max_col = 0, 0

        while que:
            n, col = que.popleft()
            groups[col].append(n.val)

            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if n.left:
                que.append((n.left, col - 1))

            if n.right:
                que.append((n.right, col + 1))

        traversal = []
        # O (n lgn)
        for k in sorted(groups.keys()):
            traversal.append(groups.get(k))

        # O (n)
        '''
        for c in range(min_col, max_col+1):
            traversal.append(groups.get(c))
        '''

        return traversal
