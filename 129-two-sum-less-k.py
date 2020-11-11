from typing import List
from collections import Counter


class Solution:
    def twoSumLessThanKv1(self, A: List[int], K: int) -> int:
        if not A:
            return -1

        # O(n lg n)
        nums = sorted(A)

        left, right, result = 0, len(nums) - 1, - 1
        for i, n in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            while left <= right:
                mid = (right - left) // 2 + left

                if mid != i and nums[mid] < K - n:
                    result = max(result, n + nums[mid])

                if nums[mid] + n >= K:
                    right = mid - 1
                else:
                    left = mid + 1

        return result

    def twoSumLessThanKv2(self, A: List[int], K: int) -> int:
        if not A:
            return -1

        # O(n + n lg n)
        nums = sorted(A)

        left, right, result = 0, len(nums) - 1, -1
        while left < right:
            s = nums[left] + nums[right]

            if s >= K:
                right -= 1
            else:
                result = max(result, s)
                left += 1

        return result

    def twoSumLessThanKv3(self, A: List[int], K: int) -> int:
        if not A:
            return -1

        counts = Counter(A)
        nums = []
        for i in range(1, 1001):
            freq = counts.get(i)
            if not i:
                continue

            nums.extend([i] * freq)

        left, right, result = 0, len(nums) - 1, -1
        while left < right:
            s = nums[left] + nums[right]

            if s >= K:
                right -= 1
            else:
                result = max(result, s)
                left += 1

        return result


print(Solution().twoSumLessThanKv1([34, 23, 1, 24, 75, 33, 54, 8], 60))
