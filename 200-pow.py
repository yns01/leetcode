class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n == 1:
            return x

        if n < 0:
            return self.myPow(1/x, -n)

        # x^10 = x^5 * x^5
        # x^11 = x^5 * x^5 * x
        # TC = O(log n), SC = O(log n)
        half = self.myPow(x, n // 2)
        result = half * half

        if n % 2 == 0:
            return result
        else:
            return result * x


print(Solution().myPow(2.00000, 3))
print(Solution().myPow(2.00000, 4))
print(Solution().myPow(2.00000, -4))
