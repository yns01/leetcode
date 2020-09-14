from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3:
            return -1

        total_sum = sum(nums)
        running_sum = 0
        for i, n in enumerate(nums):
            right_sum = total_sum - running_sum - n
            if running_sum == right_sum:
                return i

            running_sum += n

        return -1


print(Solution().pivotIndex([2, 1, 3, 5, 4, 7, 4]))
print(Solution().pivotIndex([7, -1, -2, 1, -3, -2]))
print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
print(Solution().pivotIndex([-1, -1, 0, 1, 1, 0]))
