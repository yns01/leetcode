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
