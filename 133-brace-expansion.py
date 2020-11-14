from typing import List


class Solution:
    def expand(self, S: str) -> List[str]:
        def recurse(string: str, candidate: List[str]):
            if not string:
                self.result.append(''.join(candidate))
                return

            index, options = 0, []
            if string[index] == '{':
                c = string[index]

                while c != '}':
                    if c.isalpha():
                        options.append(c)
                    index += 1
                    c = string[index]

                for o in options:
                    recurse(string[index+1:], candidate + [o])

            else:
                recurse(string[1:], candidate + [string[0]])

        if not S:
            return []

        self.result = []
        recurse(S, [])
        return sorted(self.result)


print(Solution().expand("{a,b}c{d,e}f"))
