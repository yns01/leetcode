from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ''

        adjency_list = {c: [] for word in words for c in word}

        for w1, w2 in zip(words, words[1:]):
            for i in range(len(min(w1, w2, key=len))):
                if len(w1) > len(w2) and w1.startswith(w2):
                    return ''
                if w1[i] != w2[i]:
                    adjency_list[w1[i]].append(w2[i])
                    break

        seen, order = {}, []

        VISITING, VISITED = 0, 1

        def visit(vertex):
            seen[vertex] = VISITING

            for adj in adjency_list[vertex]:
                if adj in seen and seen[adj] == VISITING:
                    # We have cycle, stop the search
                    return False

                if adj not in seen and not visit(adj):
                    return False

            seen[vertex] = VISITED
            order.append(vertex)
            return True

        for vertex in adjency_list:
            if vertex not in seen:
                if not visit(vertex):
                    return ''

        return ''.join(reversed(order))


print(Solution().alienOrder(
    ["ab", "abc"]
))
