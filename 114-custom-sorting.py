import math
from collections import Counter


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        order = {}
        for i, c in enumerate(S):
            order[c] = i

        # All character for which we have an order must go first followed by the
        # remaining ones. For those, we give them an order of Infinity and they'll
        # end up at the end of the list.
        sorted_list = sorted(T, key=lambda c: order.get(c, math.inf))
        return ''.join(sorted_list)

    def customSortStringv2(self, S: str, T: str) -> str:
        chars = Counter(T)

        custom_sorted = []

        for c in S:
            count = chars.get(c)
            if count:
                custom_sorted.extend([c] * count)

            del chars[c]

        for k, v in chars.items():
            custom_sorted.extend([k] * v)

        return ''.join(custom_sorted)


print(Solution().customSortString('cba', 'abcd'))
