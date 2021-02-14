class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return ''

        result = []
        for c in s:
            if not result:
                result.append(c)
            elif result[-1] == c:
                result.pop()
            else:
                result.append(c)

        return ''.join(result)


print(Solution().removeDuplicates("abbbcddc"))
