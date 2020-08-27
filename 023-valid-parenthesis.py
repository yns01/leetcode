class Solution:
    def __init__(self):
        self.stack = []

    def isValid(self, s: str) -> bool:
        if not s:
            return True

        for b in s:
            if self.is_opener(b):
                self.stack.append(b)
            else:
                if not self.stack:
                    return False

                if self.get_opener(b) != self.stack.pop():
                    return False

        return len(self.stack) == 0

    def is_opener(self, bracket: str) -> bool:
        return bracket == '(' or bracket == '[' or bracket == '{'

    def is_closer(self, bracket: str) -> bool:
        return not self.is_opener(bracket)

    def get_opener(self, closer) -> str:
        if closer == '}':
            return '{'
        elif closer == ')':
            return '('
        elif closer == ']':
            return '['
        else:
            raise Exception("not a valid closer")


s = Solution()

input = '()'
print(Solution().isValid(input))
input = '()[]{}'
print(Solution().isValid(input))
input = '(]'
print(Solution().isValid(input))
input = '([)]'
print(Solution().isValid(input))
input = '{[]}'
print(Solution().isValid(input))
input = '['
print(Solution().isValid(input))
