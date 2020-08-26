from typing import List
import math


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum, max_sum = 0, -math.inf

        for n in nums:
            if n > running_sum + n:
                running_sum = n
            else:
                running_sum += n

            if running_sum > max_sum:
                max_sum = running_sum

        return max_sum


print(Solution().maxSubArray([3]))
