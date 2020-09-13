class Solution:
    def myAtoi(self, input: str) -> int:
        to_convert = input.lstrip()
        if not to_convert:
            return 0

        def is_sign(c):
            return c == "+" or c == '-'

        sign = 1
        if is_sign(to_convert[0]):
            sign = -1 if to_convert[0] == '-' else 1
            to_convert = to_convert[1:]

        result = 0
        for c in to_convert:
            if not c.isdigit():
                break

            result = result * 10 + int(c)

        result *= sign

        result = min(2**31-1, result)
        result = max(-2**31, result)

        return result


s = Solution()
print(s.myAtoi("-5-"))
