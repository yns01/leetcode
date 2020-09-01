from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []

        triplets = []
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            if i != 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue

            res = self.find_zero_sum_pairs(sorted_nums, i+1,
                                           len(sorted_nums)-1, sorted_nums[i])
            if res:
                triplets.extend(res)

        return triplets

    def find_zero_sum_pairs(self, nums: List[int], left: int, right: int, first_term: int):
        triplets = []
        while left < right:
            s = first_term + nums[left] + nums[right]
            if s == 0:
                current_left_value = nums[left]
                current_right_value = nums[right]

                triplets.append(
                    [first_term, current_left_value, current_right_value])

                while left < right and nums[left] == current_left_value:
                    left += 1

                while left < right and current_right_value == nums[right]:
                    right -= 1

            if s < 0:
                left += 1
            if s > 0:
                right -= 1

        return triplets

    def threeSumV2(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        sorted_nums = sorted(nums)
        triplets = []
        for i in range(len(sorted_nums) - 2):
            if i != 0 and sorted_nums[i-1] == sorted_nums[i]:
                continue

            first_term = sorted_nums[i]
            seen = set()

            # Since in Python you can not move forward the loop, we keep track of the last time
            # we found a 0 sum. In the next iteration, if the second term is the same as the
            # previous one, we just continue looping
            last_second_term = None
            for j in range(i+1, len(sorted_nums)):
                second_term = sorted_nums[j]
                if last_second_term is not None and last_second_term == second_term:
                    continue

                third_term = 0 - (first_term+second_term)
                if third_term in seen:
                    triplets.append([first_term, second_term, third_term])
                    last_second_term = second_term
                else:
                    seen.add(second_term)

        return triplets


print(Solution().threeSumV2([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSumV2([0, 0, 0, 0]))
