from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        for i in range(len(nums)):
            current_number = nums[i]
            final_position = current_number - 1

            # Swap until we find that the number we're about to WITH, is already at it's rightful position.
            # In this case, we found a duplicate, so we just stop here.
            while current_number != nums[final_position]:
                nxt = nums[final_position]
                nums[final_position] = current_number

                current_number = nxt
                final_position = nxt-1

        res = []
        for i, n in enumerate(nums):
            if n != i+1:
                res.append(i+1)

        return res

    def findDisappearedNumbersV1(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= -1

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)

        return res

    def findDisappearedNumbersV2(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        for n in nums:
            nums[(n-1) % len(nums)] += len(nums)

        res = []
        for i, n in enumerate(nums):
            if n <= len(nums):
                res.append(i+1)

        return res


print(Solution().findDisappearedNumbersV2([4, 3, 2, 7, 8, 2, 3, 1]))
