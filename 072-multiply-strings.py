import collections


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return ''

        term1 = min(num1, num2, key=len)
        term2 = num2 if term1 == num1 else num1

        result, carry, multiplier = 0, 0, 1

        for t1 in reversed(term1):
            row_digits = collections.deque()

            for t2 in reversed(term2):
                d = int(t2) * int(t1) + carry
                carry = d // 10
                d %= 10

                row_digits.appendleft(str(d))
            if carry:
                row_digits.appendleft(str(carry))
                carry = 0

            rd = int(''.join(row_digits))
            rd *= multiplier
            result += rd
            multiplier *= 10

        return str(result)


print(Solution().multiply('123', '456'))
