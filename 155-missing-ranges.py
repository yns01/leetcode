from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            return [self.format_range(lower, upper)]

        missing = []
        if nums[0] > lower:
            missing.append(self.format_range(lower, nums[0] - 1))

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                missing.append(self.format_range(nums[i-1] + 1, nums[i] - 1))

        if nums[-1] < upper:
            missing.append(self.format_range(nums[-1] + 1, upper))

        return missing

    def format_range(self, start, end):
        if start == end:
            return str(start)
        else:
            return f"{start}->{end}"


print(Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99))
