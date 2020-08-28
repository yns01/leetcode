from typing import List


class Solution:
    def groupAnagrams(self, anagrams: List[str]) -> List[List[str]]:
        if not anagrams:
            return []

        buckets = {}
        for anagram in anagrams:
            sorted_anagram = ''.join(sorted(anagram))
            if sorted_anagram in buckets:
                buckets[sorted_anagram].append(anagram)
            else:
                buckets[sorted_anagram] = [anagram]

        return list(buckets.values())  # Same as:
        # groupped_anagrams = []
        # for _, v in buckets.items():
        #     groupped_anagrams.append(v)

    def groupAnagrams2(self, anagrams: List[str]) -> List[List[str]]:
        if not anagrams:
            return []

        buckets = {}
        for anagram in anagrams:
            k = self._get_count(anagram)
            if k in buckets:
                buckets[k].append(anagram)
            else:
                buckets[k] = [anagram]

        return list(buckets.values())

    def _get_count(self, anagram: str):
        counts = [0] * 26
        for c in anagram:
            counts[ord(c) - ord('a')] += 1

        return tuple(counts)


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))
