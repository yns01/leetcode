# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return None

        current, stack, count = root, [], 0
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                visited = stack.pop()
                count += 1
                if count == k:
                    return visited.val

                current = visited.right

        return None
