from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def recurse(string, words):
            if not string:
                return True

            if string in self.cache:
                return self.cache[string]

            # We add +1 as string[:i] excludes i.
            for i in range(len(string) + 1):
                if string[:i] in words:
                    found = recurse(string[i:], words)
                    if found:
                        self.cache[string] = True
                        return True

            self.cache[string] = False
            return False

        self.cache = {}

        return recurse(s, set(wordDict))


print(Solution().wordBreak('applepenal', ['apple', 'pen', 'pena', 'l']))
print(Solution().wordBreak('applepenapple', ['apple', 'pen']))
