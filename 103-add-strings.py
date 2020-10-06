class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1 and not num2:
            return ''

        i1, i2 = len(num1) - 1, len(num2) - 1

        result = []
        carry = 0
        while i1 >= 0 or i2 >= 0:
            d1 = ord(num1[i1]) - ord('0') if i1 >= 0 else 0
            d2 = ord(num2[i2]) - ord('0') if i2 >= 0 else 0

            d = d1 + d2 + carry
            carry = d // 10
            d %= 10

            result.append(str(d))

            i1 -= 1
            i2 -= 1

        if carry:
            result.append(str(carry))

        return ''.join(reversed(result))


print(Solution().addStrings('123', '456'))
