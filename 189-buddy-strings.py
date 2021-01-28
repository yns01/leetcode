class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False

        if a == b:
            # If a and b are equals, we need to have at least two duplicates char
            # two swap them. If we don't have any, the len of the set will be equal to
            # the len of the string
            return not len(set(a)) == len(a)

        diffs = []
        for i in range(len(a)):
            if a[i] != b[i]:
                diffs.append(i)

        if len(diffs) != 2:
            return False

        d1, d2 = diffs
        return a[d1] == b[d2] and a[d2] == b[d1]


print(Solution().buddyStrings("ab", "ba"))
print(Solution().buddyStrings("ab", "ab"))
print(Solution().buddyStrings("aa", "aa"))
print(Solution().buddyStrings("aaaaaaabc", "aaaaaaacb"))
print(Solution().buddyStrings("", "aa"))
