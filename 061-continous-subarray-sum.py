from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int):
        sums = {0: -1}
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += num

            if k != 0:
                running_sum %= k

            if running_sum in sums:
                if i - sums[running_sum] >= 2:
                    return True

            else:
                sums[running_sum] = i

        return False


print(Solution().checkSubarraySum([0, 0, 0, 0], 6))
