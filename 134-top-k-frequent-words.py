from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        freq_to_elements = [[] for _ in range(len(words) + 1)]

        for word, freq in counts.items():
            freq_to_elements[freq].append(word)

        result = []

        index, elements = len(freq_to_elements) - 1, 0
        while elements < k:
            result.extend(sorted(freq_to_elements[index]))
            elements += len(freq_to_elements[index])

            index -= 1

        return result[:k]


print(Solution().topKFrequent(
    ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
