class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True

        stack, stars = [], []

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if not stack and not stars:
                    return False

                if stack:
                    stack.pop()
                else:
                    stars.pop()
            else:
                stars.append(i)

        # At the top of the stack, we can find the right most elements of the string
        # Thus, if the index of the stack is greater than the rightmost star, it means
        # we don't have any stars at the right of the bracket in the string, making it
        # invalid as we can't use a star to compensate it.
        while stack and stars:
            if stack.pop() > stars.pop():
                return False

        return len(stack) == 0


print(Solution().checkValidString("*(()*"))
