from typing import List
import math


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        closest = math.inf

        nums.sort()
        for i, first_member in enumerate(nums):
            current_closest = self.find_pair(
                nums,
                i+1,
                len(nums) - 1,
                target,
                first_member,
            )

            if current_closest == target:
                return target

            if abs(target - current_closest) < abs(target - closest):
                closest = current_closest

        return closest

    def find_pair(self, nums: List[int], left: int, right: int, target: int, first_member: int) -> int:
        closest = math.inf

        while left < right:
            s = first_member + nums[left] + nums[right]
            if abs(target - s) < abs(target - closest):
                closest = s

            if s == target:
                return s
            elif s < target:
                left += 1
            else:
                right -= 1

        return closest


print(Solution().threeSumClosest([0, -3, -1, 1, 2], - 1))
