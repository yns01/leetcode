from typing import List
# https://leetcode.com/problems/contiguous-array/


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Approach: We keep a counter going up or down as we encounter 0 and 1s.
        # At any point, if we have seen the counter value previously, it means that
        # the number of ones and zeros are balanced between the two occurrences of that counter
        # value.

        count = 0
        count_dict = {0: -1}

        max_len = 0
        for i, n in enumerate(nums):
            if n == 1:
                count += 1
            else:
                count -= 1

            if count in count_dict:
                max_len = max(max_len, i - count_dict[count])
            else:
                count_dict[count] = i

        return max_len


print(Solution().findMaxLength([0, 1, 0, 0, 1]))
