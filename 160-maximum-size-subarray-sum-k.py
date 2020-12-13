from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        running_sum, sums = 0, {0: -1}
        max_len = 0

        for i, n in enumerate(nums):
            running_sum += n

            complement = running_sum - k
            if complement in sums:
                max_len = max(max_len, i - sums[complement])

            if running_sum not in sums:
                sums[running_sum] = i

        return max_len


print(Solution().maxSubArrayLen([1, -1, 5, -2, 3], 3))
