from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        running_sum, sums = 0, {}
        max_len = 0

        for i, n in enumerate(nums):
            running_sum += n

            complement = running_sum - k

            # If the complement is 0, it means that the running sum from
            # the start of the array to i equals k. In that case, the len of
            # the sub array is i+1
            if complement == 0:
                max_len = max(max_len, i+1)
            # Otherwise, the len of the subarray is i - sums[complement]
            # which is the index of the complement.
            elif complement in sums:
                max_len = max(max_len, i - sums[complement])

            if running_sum not in sums:
                sums[running_sum] = i

        return max_len


print(Solution().maxSubArrayLen([1, -1, 5, -2, 3], 3))
