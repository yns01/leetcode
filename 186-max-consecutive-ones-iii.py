from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        window_start, zero_count, res = 0, 0, 0

        for window_end in range(len(A)):
            n = A[window_end]

            if n == 0:
                zero_count += 1

            # We allow K zeroes to be flipped
            # If zero_count is greater than K,
            # our contract is violated.
            while zero_count > K:
                if A[window_start] == 0:
                    zero_count -= 1

                window_start += 1

            res = max(res, window_end - window_start + 1)

        return res


print(Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution().longestOnes(
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
