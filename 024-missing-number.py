from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # The maximum number in a full array is len(n) - 1
        # However, we known that we're missing one element in the array.
        # The maximum value is then len(n)-1+1
        max_number = len(nums)
        expected_sum = (max_number * (max_number + 1)) // 2
        computed_sum = sum(nums)

        return expected_sum - computed_sum


print(Solution().missingNumber([0, 1, 2, 3, 4, 5, 6, 7]))
