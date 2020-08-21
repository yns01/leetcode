from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if not nums:
            return

        current_position = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if nums[current_position] == 0:
                    nums[i], nums[current_position] = nums[current_position], nums[i]

                current_position += 1

        return


s = Solution()
input = [1, 2, 3, 0, 0, 5]
s.moveZeroes(input)
print(input)
