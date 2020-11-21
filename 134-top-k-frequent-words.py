from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        freq_to_elements = [[] for _ in range(len(words) + 1)]

        for word, freq in counts.items():
            freq_to_elements[freq].append(word)

        result = []

        index = len(freq_to_elements) - 1
        while len(result) < k:
            result.extend(sorted(freq_to_elements[index]))
            index -= 1

        return result[:k]

    def topKFrequentV1(self, words: List[str], k: int) -> List[str]:
        frequencies = Counter(words)

        heap = []
        for word, freq in frequencies.items():
            heap.append((-freq, word))

        heapq.heapify(heap)

        result = []
        while len(result) < k:
            result.append(heapq.heappop(heap)[1])

        return result


print(Solution().topKFrequent(
    ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))


print(Solution().topKFrequentV1(
    ["i", "love", "leetcode", "i", "love", "coding"], 2))
