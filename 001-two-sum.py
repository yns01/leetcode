from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        values = {}

        for i in range(len(nums)):
            complement = target-nums[i]
            if complement not in values:
                values[nums[i]] = i
                continue

            return [i, values.get(complement)]

        return []


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
