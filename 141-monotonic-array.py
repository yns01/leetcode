from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        is_increasing = None
        for i in range(1, len(nums)):
            # We don't know yet if the array is asc or desc
            if is_increasing is None:
                if nums[i-1] < nums[i]:
                    is_increasing = True
                elif nums[i-1] > nums[i]:
                    is_increasing = False

                continue

            if (is_increasing and nums[i-1] > nums[i]) or (not is_increasing and nums[i-1] < nums[i]):
                return False

        return True


print(Solution().isMonotonic([1, 2, 2, 3]))
print(Solution().isMonotonic([1, 1, 2]))
