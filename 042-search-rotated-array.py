from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums)-1

        while left <= right:
            mid = (right - left) // 2 + left

            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                # left part is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right part is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


print(Solution().search([3, 1], 1))
