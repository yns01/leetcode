from typing import List


class Solution:
    def canThreePartsEqualSum(self, nums: List[int]) -> bool:
        if not nums:
            return False

        total_sum = sum(nums)
        if total_sum % 3 != 0:
            return False

        partition_sum = total_sum // 3
        running_sum, partition_sum_count = 0, 0
        for n in nums:
            running_sum += n
            if running_sum == partition_sum:
                running_sum = 0
                partition_sum_count += 1

        return partition_sum_count >= 3


print(Solution().canThreePartsEqualSum([1, -1, 1, -1]))
print(Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
print(Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))
print(Solution().canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))
