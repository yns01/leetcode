from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return []

        def recurse(string, candidates):
            if not string:
                splits.append(' '.join(candidates))
                return True

            if string in cache:
                return cache[string]

            result = False
            for i in range(len(string) + 1):
                w = string[:i]
                if w in words:
                    if recurse(string[i:], candidates + [w]):
                        result = True

            if not result:
                cache[string] = False

            return result

        words, splits, cache = set(wordDict), [], {}

        recurse(s, [])

        return splits


print(Solution().wordBreak("catsanddog", [
      "cat", "cats", "and", "sand", "dog"]))
print(Solution().wordBreak("pineapplepenapple", [
      "apple", "pen", "applepen", "pine", "pineapple"]))
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
