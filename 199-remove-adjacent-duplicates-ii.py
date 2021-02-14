class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s:
            return ''

        to_insert = []
        for c in s:
            if not to_insert or to_insert[-1][0] != c:
                to_insert.append([c, 1])
            else:
                _, count = to_insert[-1]
                if count + 1 < k:
                    to_insert[-1][1] += 1
                else:
                    to_insert.pop()

        result = []
        for c, freq in to_insert:
            result.append(c * freq)

        return ''.join(result)


print(Solution().removeDuplicates("abcd", 2))
print(Solution().removeDuplicates("deeedbbcccbdaa", 3))
print(Solution().removeDuplicates("pbbcggttciiippooaais", 2))
