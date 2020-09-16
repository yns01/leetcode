import collections


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pa, pb = len(a) - 1, len(b) - 1

        carry = 0
        result = collections.deque()

        while pa >= 0 and pb >= 0:
            s = (int(a[pa]) + int(b[pb]) + carry)
            carry = s // 2
            s %= 2

            result.appendleft(str(s))

            pa -= 1
            pb -= 1

        while pa >= 0:
            s = (int(a[pa]) + carry)
            carry = s // 2
            s %= 2

            result.appendleft(str(s))
            pa -= 1

        while pb >= 0:
            s = (int(b[pb]) + carry)
            carry = s // 2
            s %= 2

            result.appendleft(str(s))
            pb -= 1

        if carry:
            result.appendleft(str(carry))

        return ''.join(list(result))


print(Solution().addBinary('10101010', '1101'))
