from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        if not strings:
            return []

        '''
        Two strings belong to the same shifting group when the difference between its char
        is the same.
        Not to be confused by how many times it was shifted.
        'abc' and 'lmn' they belong to the same shift sequence because (m-l) = 1 and (n-m) = 1
        'ceg' and 'egi'
        'cef' and 'egh' e-c = 2 f-e = 1
        '''
        groups = {}
        for string in strings:
            key = []
            for i in range(1, len(string)):
                current_char = string[i]
                prev_char = string[i-1]
                key.append((ord(current_char) - ord(prev_char)) % 26)

            key = tuple(key)
            if key in groups:
                groups[key].append(string)
            else:
                groups[key] = [string]

        return groups.values()


print(Solution().groupStrings(
    ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z", 'ceg', 'egi']))
