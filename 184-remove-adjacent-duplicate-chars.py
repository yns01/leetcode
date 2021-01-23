class Solution:
    def removeDuplicates(self, S: str) -> str:
        if not S:
            return S

        res = []

        i = 0
        while i < len(S):
            current_char = S[i]
            if res and res[-1] == current_char:
                res.pop()
            else:
                res.append(current_char)

            i += 1

        return ''.join(res)


print(Solution().removeDuplicates("abbbcddc"))
