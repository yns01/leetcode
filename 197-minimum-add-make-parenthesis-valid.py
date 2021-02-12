class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0

        result, counter = 0, 0
        for n in s:
            if n == '(':
                counter += 1
            elif n == ')':
                if counter:
                    counter -= 1
                else:
                    result += 1

        result += counter

        return result

    def minAddToMakeValidV1(self, s: str) -> int:
        if not s:
            return 0

        result, stack = 0, []
        for i, n in enumerate(s):
            if n == '(':
                stack.append(i)
            elif n == ')':
                if stack:
                    stack.pop()
                else:
                    result += 1

        result += len(stack)

        return result


print(Solution().minAddToMakeValid("())"))
print(Solution().minAddToMakeValid("((("))
print(Solution().minAddToMakeValid("()"))
print(Solution().minAddToMakeValid("()))(("))
