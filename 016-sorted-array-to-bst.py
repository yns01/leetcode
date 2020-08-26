from typing import List
from collections import deque
import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order_traversal(root):
    if not root:
        return None

    in_order_traversal(root.left)
    print(root.val)
    in_order_traversal(root.right)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        return self._to_bst(nums, 0, len(nums) - 1)

    def _to_bst(self, nums: List[int], left: int, right: int):
        if left > right:
            return None

        mid = (right - left) // 2 + left
        n = TreeNode(nums[mid])

        n.left = self._to_bst(nums, left, mid-1)
        n.right = self._to_bst(nums, mid+1, right)

        return n


input = [-10, -3, 0, 5, 9]
result = Solution().sortedArrayToBST(input)
in_order_traversal(result)
