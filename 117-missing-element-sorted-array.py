from typing import List


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        '''
        https://leetcode.com/explore/learn/card/binary-search/136/template-analysis/935/
        We use the third template for this problem.
        At the end of the loop, left+1 == right.
        In our case, we know that when we start the BS, the first element after which we should
        count the missing elements cannot be the last element of the array as this case is cleared
        in the preprocessing step.
        '''
        def count_missing_elements(left, right):
            expected_elements = nums[right] - nums[left]
            actual_elements = right - left
            return expected_elements - actual_elements

        total_missing = count_missing_elements(0, len(nums) - 1)
        if total_missing < k:
            k -= total_missing
            return nums[-1] + k

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (right - left) // 2 + left
            missing_elements_left = count_missing_elements(left, mid)
            if k > missing_elements_left:
                k -= missing_elements_left
                left = mid
            else:
                right = mid

        return nums[left] + k

    def missingElementV1(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1] - 1
            if diff >= k:
                return nums[i-1] + k

            k -= diff

        return nums[-1] + k


print(Solution().missingElement([4, 7, 9, 10], 3))
