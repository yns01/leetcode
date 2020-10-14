from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        node = root
        que = deque()
        que.append(node)

        seen_empty_node_before = False
        while que:
            n = que.popleft()

            if n:

                if seen_empty_node_before:
                    return False

                que.append(n.left)
                que.append(n.right)

            else:
                seen_empty_node_before = True

        return True
