import collections


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pa, pb = len(a) - 1, len(b) - 1

        carry = 0
        result = collections.deque()

        while pa >= 0 or pb >= 0:
            da = int(a[pa]) if pa >= 0 else 0
            db = int(b[pb]) if pb >= 0 else 0

            s = da + db + carry
            carry = s // 2
            s %= 2

            result.appendleft(str(s))

            pa -= 1
            pb -= 1

        if carry:
            result.appendleft(str(carry))

        return ''.join(list(result))


print(Solution().addBinary('10101010', '1101'))
