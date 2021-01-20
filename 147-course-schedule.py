from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses or not prerequisites:
            return True

        courses = {c: [] for c in range(numCourses)}

        for req in prerequisites:
            course = req[0]
            neighbors = courses.get(course)

            for dep in req[1:]:
                neighbors.append(dep)

        seen, VISITING, VISITED = {}, 0, 1

        def visit(course):
            seen[course] = VISITING

            for dep in courses.get(course, []):
                if dep not in seen:
                    cycle = visit(dep)
                    if cycle:
                        return True

                elif seen[dep] == VISITING:
                    return True

            seen[course] = VISITED
            return False

        for c in courses:
            if c not in seen:
                cycle = visit(c)
                if cycle:
                    return False

        return True


print(Solution().canFinish(2, [[1, 0], [0, 1]]))
print(Solution().canFinish(2, [[1, 0]]))
