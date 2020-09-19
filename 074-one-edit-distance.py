class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False

        one_edit = False
        s_index, t_index = 0, 0

        if abs(len(s) - len(t)) > 1:
            return False

        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
                t_index += 1
                continue

            if one_edit:
                return False

            one_edit = True
            if len(s) < len(t):
                t_index += 1
            elif len(s) > len(t):
                s_index += 1
            else:
                t_index += 1
                s_index += 1

        if s_index == len(s) and t_index == len(t):
            return True

        # At this point, there's exactly one character difference between the two strings.
        # If we already made an edit and have one character left, it's ont a one edit distance
        # Otherwise, we not made an edit yet and consider the last character is an edit.
        return not one_edit


print(Solution().isOneEditDistance('teacher', 'tache'))
