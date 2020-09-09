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

    def sort_colors(self, nums: List[int]) -> None:
        if not nums:
            return None

        left, right, current = 0, len(nums)-1, 0

        while current <= right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == 2:
                nums[right], nums[current] = nums[current], nums[right]
                right -= 1
            else:
                current += 1


i = [0, 0, 0, 0, 1, 1, 2, 0, 0]
Solution().sort_colors(i)
print(i)
