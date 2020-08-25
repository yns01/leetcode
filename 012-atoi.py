class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0

        digits = ""

        for c in str:
            if (c != "+" and c != "-" and not c.isdigit()):
                if digits:
                    break
                if not digits and c == ' ':
                    continue
                else:
                    return 0
            else:
                digits += c

        result, multiplier = 0, 1
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == '-':
                result *= -1
            elif digits[i] == '+':
                result *= 1
            else:
                result += multiplier * int(digits[i])
                multiplier *= 10

        if result < INT_MIN:
            result = INT_MIN
        elif result > INT_MAX:
            result = INT_MAX

        return result


s = Solution()
print(s.myAtoi("91283472332"))
