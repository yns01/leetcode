
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return s

        stack = []
        indices_to_remove = set()

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    indices_to_remove.add(i)

        while stack:
            indices_to_remove.add(stack.pop())

        result = []

        for i, c in enumerate(s):
            if i in indices_to_remove:
                continue
            else:
                result.append(c)

        return ''.join(result)

    def minRemoveToMakeValidv1(self, s: str) -> str:
        if not s:
            return s

        stack = []
        result = list(s)

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    result[i] = ''

        while stack:
            result[stack.pop()] = ''

        return ''.join(result)


Solution().minRemoveToMakeValid('A(B)C((')
