class Solution:
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        return self._cbs(n, 0)

    def _cbs(self, n, climbed):
        if climbed > n:
            return 0

        if climbed == n:
            return 1

        if climbed in self.memo:
            return self.memo.get(climbed)

        count = self._cbs(n, climbed + 1) + self._cbs(n, climbed + 2)
        self.memo[climbed] = count
        return count


print(Solution().climbStairs(3))
