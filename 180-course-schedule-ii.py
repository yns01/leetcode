from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {n: [] for n in range(numCourses)}

        if not prerequisites:
            return graph.keys()

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        def visit(course, attended):
            seen[course] = VISITING

            for prereq in graph[course]:
                if prereq not in seen:
                    if visit(prereq, attended):
                        return True
                elif seen[prereq] == VISITING:
                    return True

            attended.append(course)
            seen[course] = VISITED

            return False

        seen, VISITING, VISITED = {}, 0, 1
        res = []
        for course in graph:
            if course in seen:
                continue

            attended = []
            has_cycle = visit(course, attended)
            if has_cycle:
                return []

            res.extend(attended)

        return res


print(Solution().findOrder(2, [[1, 0]]))
print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(Solution().findOrder(
    7, [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]))

print(Solution().findOrder(1, []))
