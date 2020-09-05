from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        starting_range = self.find(nums, target, True)
        if starting_range == -1:
            return [-1, -1]

        ending_range = self.find(nums, target, False)
        return [starting_range, ending_range]

    def find(self, nums: List[int], target: int, first: bool) -> int:
        left, right, target_position = 0, len(nums) - 1, -1

        while left <= right:
            mid = (right - left) // 2 + left

            if nums[mid] == target:
                target_position = mid
                if first:
                    right = mid-1
                else:
                    left = mid+1
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1

        return target_position


print(Solution().searchRange([5, 6, 6, 6, 6, 7, 8, 9, 10, 15, 2], 6))
