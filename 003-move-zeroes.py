from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if not nums:
            return

        first_swapable_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[first_swapable_pos] == 0:
                nums[i], nums[first_swapable_pos] = nums[first_swapable_pos], nums[i]
                first_swapable_pos += 1

            if nums[first_swapable_pos] != 0:
                first_swapable_pos += 1
        return

    def moveZeroesBeginning(self, nums: List[int]) -> None:
        if not nums:
            return None

        first_swapable_pos = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != 0 and nums[first_swapable_pos] == 0:
                nums[i], nums[first_swapable_pos] = nums[first_swapable_pos], nums[i]
                first_swapable_pos -= 1

            if nums[first_swapable_pos] != 0:
                first_swapable_pos -= 1


s = Solution()
input = [0, 0, 0, 3, 12]
s.moveZeroes(input)
print(input)

input = [0, 1, 2, 3, 5, 0, 4, 7, 6]
s.moveZeroesBeginning(input)
print(input)
