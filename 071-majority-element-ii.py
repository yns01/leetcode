from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) < 2:
            return nums

        candidate_1, candidate_2 = None, None
        c1, c2 = 0, 0

        for current_num in nums:
            # If one of the counter went to zero, we must select the current number as candidate.
            # However, we must ensure that current number is not already a candidate.
            if c1 == 0 and current_num != candidate_2:
                candidate_1 = current_num
            elif c2 == 0 and current_num != candidate_1:
                candidate_2 = current_num

            if current_num == candidate_1:
                c1 += 1
            elif current_num == candidate_2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1

        res = []
        if nums.count(candidate_1) > len(nums) / 3:
            res.append(candidate_1)

        if nums.count(candidate_2) > len(nums) / 3:
            res.append(candidate_2)

        return res


print(Solution().majorityElement([1, 2, 2, 3, 2, 1, 1, 3]))
print(Solution().majorityElement([3, 2, 3]))
print(Solution().majorityElement(
    [1, 3, 3, 2, 2, 4, 3, 3, 5, 5, 6, 3, 3, 7, 7]))
