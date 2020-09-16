from typing import List
import math


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        selected_word = None
        position = 0
        min_distance = math.inf

        for i, w in enumerate(words):
            if w != word1 and w != word2:
                continue

            if not selected_word:
                selected_word = w
                position = i
                continue

            if w != selected_word:
                min_distance = min(min_distance, i - position)

            selected_word = w
            position = i

        return min_distance

    def shortestDistanceV2(self, words: List[str], word1: str, word2: str) -> int:
        p1, p2 = None, None
        min_distance = len(words)

        for i, w in enumerate(words):
            if w == word1:
                p1 = i
            elif w == word2:
                p2 = i

            if p1 is not None and p2 is not None:
                min_distance = min(abs(p2-p1), min_distance)

        return min_distance


print(Solution().shortestDistance(
    ['a', 'b', 'z', 'e', 'f', 'c', 'j', 'c', 'f', 'a', 'c'], 'f', 'z'))
