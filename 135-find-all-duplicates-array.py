from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        for n in nums:
            nums[(n - 1) % len(nums)] += len(nums)

        res = []
        for i, n in enumerate(nums):
            if len(nums) * 2 < n:
                res.append(i+1)

        return res


print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
