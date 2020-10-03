from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not words:
            return True

        order_dict = {}
        for i, c in enumerate(order):
            order_dict[c] = i

        for word1, word2 in zip(words, words[1:]):
            if len(word1) > len(word2) and word1.startswith(word2):
                return False

            for i in range(min(len(word1), len(word2))):
                c1 = word1[i]
                c2 = word2[i]

                if c1 == c2:
                    continue

                if order_dict.get(c1) < order_dict.get(c2):
                    break

                return False

        return True


print(Solution().isAlienSorted(
    ['hell', 'hello', 'world', 'wowir', 'wow', 'wowit'], 'abcdefghijklmnopqrstuvwxyz'))
