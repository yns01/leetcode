from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 1000000000 + 7

        sorted_nums = sorted(nums)
        res, left, right = 0, 0, len(sorted_nums) - 1

        while left <= right:
            if sorted_nums[right] + sorted_nums[left] > target:
                right -= 1
            else:
                res += pow(2, right - left, mod)
                left += 1

        return res % mod


print(Solution().numSubseq([3, 3, 6, 8], 10))
