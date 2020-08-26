# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(vers):
    return vers >= 9


class Solution:
    def firstBadVersion(self, n) -> int:
        left, right = 0, n

        first_bv = -1
        while left <= right:
            mid = (right - left) // 2 + left
            ibv = isBadVersion(mid)
            if ibv:
                first_bv = mid
                right = mid - 1
            else:
                left = mid+1

        return first_bv


print(Solution().firstBadVersion(10))
