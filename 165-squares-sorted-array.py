from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        left, right = 0, len(nums) - 1
        res = []
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                res.append(pow(nums[left], 2))
                left += 1

            else:
                res.append(pow(nums[right], 2))
                right -= 1

        return reversed(res)


print(list(Solution().sortedSquares([-4, -1, 0, 3, 10])))
