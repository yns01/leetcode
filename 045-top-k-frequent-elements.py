from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        values_to_occ = Counter(nums)

        occ_to_values = [[] for _ in range(len(nums) + 1)]

        for num, freq in values_to_occ.items():
            occ_to_values[freq].append(num)

        tops = []
        for i in range(len(occ_to_values)-1, -1, -1):
            if len(tops) < k and occ_to_values[i]:
                while occ_to_values[i]:
                    tops.append(occ_to_values[i].pop())

        # If there are more than k occurrences for one number, we have added all of
        # them in the previous loop. Let's take only k elements.
        return tops[:k]


print(Solution().topKFrequent([4, 1, -1, 2, -1, 2, 3], 3))
