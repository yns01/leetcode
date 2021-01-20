# https://leetcode.com/problems/minimum-size-subarray-sum/

import math
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        res, rs, window_start = math.inf, 0, 0
        for window_end in range(len(nums)):
            rs += nums[window_end]

            while rs >= s:
                res = min(res, (window_end - window_start + 1))
                rs -= nums[window_start]
                window_start += 1

        return 0 if res == math.inf else res


print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
