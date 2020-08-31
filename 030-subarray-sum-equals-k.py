from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum, counts, sums = 0, 0, {0: 1}

        for i in range(len(nums)):
            running_sum += nums[i]
            complement = running_sum - k
            if complement in sums:
                counts += sums.get(complement)

            if running_sum in sums:
                sums[running_sum] += 1
            else:
                sums[running_sum] = 1

        return counts


print(Solution().subarraySum([23, 2, 4, 6], 6))
