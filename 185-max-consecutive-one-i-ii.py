from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count, count_since_flip, flipped, res = 0, 0, False, 0

        for n in nums:
            if n == 1:
                count += 1
                if flipped:
                    count_since_flip += 1

            else:
                if flipped:
                    res = max(res, count)
                    count = count_since_flip + 1
                    count_since_flip = 0
                else:
                    flipped = True
                    count += 1

        # If the last element is included in the max sequence and is a 1,
        # we have not yet computed the max in res
        return max(res, count)

    def findMaxConsecutiveOnesSlidingWindow(self, nums: List[int]) -> int:
        if not nums:
            return 0

        window_start, zeroes_count, res = 0, 0, 0

        for window_end in range(len(nums)):
            current_num = nums[window_end]

            if current_num == 0:
                zeroes_count += 1

            # Reduce window until contract is valid
            # We allow only 1 zero to be flipped, in other words
            # if zeroes_count is greater than 1, our contract
            # is not valid
            while zeroes_count > 1:
                if nums[window_start] == 0:
                    zeroes_count -= 1

                window_start += 1

            res = max(res, window_end - window_start + 1)

        return res

    def findMaxConsecutiveOnes_I(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count, res = 0, 0
        for n in nums:
            if n == 1:
                count += 1
                res = max(res, count)
            else:
                count = 0

        return res


print(Solution().findMaxConsecutiveOnes_I([1, 0, 1, 1, 0, 1]))
print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1, 1, 1, 1]))
