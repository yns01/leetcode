from typing import List
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def recurse(nums, start, end):
            if start > end:
                return None

            max_val = -math.inf
            max_pos = 0
            for i in range(start, end + 1):
                n = nums[i]

                if n > max_val:
                    max_val = n
                    max_pos = i

            root = TreeNode(max_val)
            root.left = recurse(nums, start, max_pos - 1)
            root.right = recurse(nums, max_pos + 1, end)

            return root

        if not nums:
            return None

        return recurse(nums, 0, len(nums) - 1)


print(Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]).val)
