from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        if target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        res = None
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                res = mid
                right = mid - 1

            else:
                left = mid + 1

        return res

    def searchInsertv1(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        if target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        while left + 1 < right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right = mid

            else:
                left = mid

        if nums[right] == target:
            return right

        if nums[left] == target:
            return left

        return left + 1


print(Solution().searchInsertv1([1, 3, 5, 6], 5))
print(Solution().searchInsertv1([1, 3, 5, 6], 7))
print(Solution().searchInsertv1([1, 3, 5, 6], 2))
print(Solution().searchInsertv1([1, 3, 5, 6], 0))
print(Solution().searchInsertv1([1], 0))
