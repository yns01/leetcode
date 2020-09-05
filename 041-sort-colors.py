from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if not nums:
            return None

        last_swapable_position = 0

        for i in range(len(nums)):
            if nums[i] == 0 and nums[last_swapable_position] != 0:
                nums[last_swapable_position], nums[i] = nums[i], nums[last_swapable_position]
                last_swapable_position += 1

            if nums[last_swapable_position] == 0:
                last_swapable_position += 1

        for i in range(last_swapable_position, len(nums)):
            if nums[i] == 1 and nums[last_swapable_position] == 2:
                nums[last_swapable_position], nums[i] = nums[i], nums[last_swapable_position]
                last_swapable_position += 1

            if nums[last_swapable_position] == 1:
                last_swapable_position += 1


i = [1, 0, 2, 0, 2, 1, 2, 0, 0]
Solution().sortColors(i)
print(i)
