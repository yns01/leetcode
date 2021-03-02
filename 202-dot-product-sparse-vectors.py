from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.values = {}
        for i, n in enumerate(nums):
            if n:
                self.values[i] = n

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for k, v in self.values.items():
            result += v * vec.values.get(k, 0)

        return result


class SparseVector1:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.non_zero_indices = []
        for i, n in enumerate(nums):
            if n != 0:
                self.non_zero_indices.append(i)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in self.non_zero_indices:
            res += self.nums[i] * vec.nums[i]

        return res


class SparseVector2:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for i, n in enumerate(nums):
            if n != 0:
                self.pairs.append((i, n))

    def dotProduct(self, vec: 'SparseVector') -> int:
        i1, i2 = 0, 0

        res = 0
        while i1 < len(self.pairs) and i2 < len(vec.pairs):
            if self.pairs[i1][0] == vec.pairs[i2][0]:
                res += self.pairs[i1][1] * vec.pairs[i2][1]
                i1 += 1
                i2 += 1
            elif self.pairs[i1][0] < vec.pairs[i2][0]:
                i1 += 1
            else:
                i2 += 1

        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
