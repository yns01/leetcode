from typing import List
from collections import deque


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not nums2:
            return nums1

        write_index = len(nums1) - 1
        left, right = m-1, n-1
        while left >= 0 and right >= 0:
            left_value = nums1[left]
            right_value = nums2[right]

            if left_value >= right_value:
                nums1[write_index] = left_value
                left -= 1
            else:
                nums1[write_index] = right_value
                right -= 1

            write_index -= 1

        if right >= 0:
            nums1[:write_index+1] = nums2[:right+1]
            for i in range(right, -1, -1):
                nums1[write_index] = nums2[i]
                write_index -= 1


input = [1, 2, 3, 13, 15, 20, 30, 0, 0, 0, 0, 0, 0]
input2 = [-4, -5, -25, -28, 29, 46]
Solution().merge(input, len(input)-len(input2), input2, len(input2))
print(input)
