from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right - left) // 2 + left

            # We know we found the single element, if it does not equal
            # nor its predecessor or follower.
            # However, it may be the first or last element in the array.
            # If mid - 1 or mid + 1 is out of bounds, we're looking at the first or last
            # elements and we finished our search anyways. So we just return that element.
            if mid - 1 < 0 or mid + 1 >= len(nums):
                return nums[mid]

            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]

            # Check if mid belongs to the right or left part of the array
            if nums[mid-1] == nums[mid]:
                # If it belongs to the left part, we check if the left part is even, and if it is,
                # we must go right.
                # Since we know that num[mid] belongs to the left part,
                # we reduce the search space to [mid+1, right]
                # It it's not even, it means that the left part (with mid included) is odd and we
                # have one non duplicated element there. So we reduce our search space to [left, mid]

                if (mid - left + 1) % 2 == 0:
                    left = mid + 1
                else:
                    right = mid
            else:
                if (right - mid + 1) % 2 == 0:
                    right = mid - 1
                else:
                    left = mid

        return -1


print(Solution().singleNonDuplicate([1, 1, 2]))
print(Solution().singleNonDuplicate([1, 2, 2]))
print(Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
