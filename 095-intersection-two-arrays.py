from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 and not nums2:
            return []

        elements = set(nums1)
        res = []
        for n in nums2:
            if n in elements:
                res.append(n)
                elements.remove(n)

        return res

    def intersection_v2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 and not nums2:
            return []

        nums1.sort()
        nums2.sort()

        res = []
        i1, i2 = 0, 0
        while i1 < len(nums1) and i2 < len(nums2):
            n1 = nums1[i1]
            n2 = nums2[i2]

            if n1 == n2:
                res.append(n1)
                while i1 < len(nums1) and nums1[i1] == n1:
                    i1 += 1

                while i2 < len(nums2) and nums2[i2] == n2:
                    i2 += 1
            elif n1 < n2:
                i1 += 1
            else:
                i2 += 1

        return res


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(Solution().intersection_v2(nums1, nums2))
