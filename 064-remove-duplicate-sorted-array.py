from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        fast = 1
        last_non_duplicate = 0
        while fast < len(nums):
            if nums[fast] == nums[last_non_duplicate]:
                fast += 1
            else:
                nums[last_non_duplicate+1] = nums[fast]
                fast += 1
                last_non_duplicate += 1

        return last_non_duplicate+1


# input = [2, 2, 3, 4, 4, 5, 6, 7, 8, 8, 10]
input = [2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]
# input = [2, 2, 3]
l = Solution().removeDuplicates(input)

print(l, input[0:l])
