from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []

        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1, right+1]
            elif s < target:
                left += 1
            else:
                right -= 1

        return []


print(Solution().twoSum([-4, -2, -1, 0, 1], 0))
