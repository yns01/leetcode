from typing import List
# https://leetcode.com/problems/kth-missing-positive-number/


class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        # Returns the number of elements missing between [1...i]
        def missing_from_1(i):
            # the array is sorted, so nums[i] is the maximum possible value we can have
            # (if the array ended at i)
            # In other words, the number of elements we expect is nums[i] (+1 if 0 was the first missing)
            # To get the missing element count, we substract the elements we already have.
            # At index i, we have i+1 elements.
            return nums[i] - (i + 1)

        i = len(nums) - 1
        total_missing = missing_from_1(i)
        if total_missing < k:
            k -= total_missing
            return nums[-1] + k

        missing_before_nums0 = missing_from_1(0)
        if missing_before_nums0 >= k:
            return k

        k -= missing_before_nums0

        # Returns the number of missing elements between index left and right
        # To get this formula, we can compute the missing from [1...right] - missing from [1...left]
        # nums[right] - (right+1) - (nums[left] - (left + 1))
        # = nums[right] - right - 1 - (nums[left] - left - 1)
        # = nums[right] - right - 1 - nums[left] + left + 1
        # = nums[right] - nums[left] - (right - left)
        def missing(left, right):
            return nums[right] - nums[left] - (right - left)

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (right - left) // 2 + left

            missing_count = missing(left, mid)

            if missing_count < k:
                k -= missing_count
                left = mid
            else:
                right = mid

        return nums[left] + k


print(Solution().findKthPositive([2, 3, 4, 7, 11], 5))
print(Solution().findKthPositive([7, 17, 22, 26, 34], 9))
print(Solution().findKthPositive([2], 1))
