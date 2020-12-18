from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i1, i2 = 0, 0
        char_index1, char_index2 = 0, 0

        while i1 < len(word1) and i2 < len(word2):
            if word1[i1][char_index1] != word2[i2][char_index2]:
                return False

            if char_index1 == len(word1[i1]) - 1:
                char_index1 = 0
                i1 += 1
            else:
                char_index1 += 1

            if char_index2 == len(word2[i2]) - 1:
                char_index2 = 0
                i2 += 1
            else:
                char_index2 += 1

        return i1 == len(word1) and i2 == len(word2)


print(Solution().arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
