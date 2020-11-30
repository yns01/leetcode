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
            total_courses = 0
            seen[course] = VISITING

            for dep in courses.get(course, []):
                if dep not in seen:
                    cycle, count = visit(dep)
                    if cycle:
                        return (True, -1)

                    total_courses += count
                elif seen[dep] == VISITING:
                    return (True, -1)

            seen[course] = VISITED
            return (False, total_courses + 1)

        attended = 0
        for c in courses:
            if c not in seen:
                cycle, count = visit(c)
                if not cycle:
                    attended += count

                if attended >= numCourses:
                    return True

        return attended >= numCourses


print(Solution().canFinish(2, [[1, 0], [0, 1]]))
print(Solution().canFinish(2, [[1, 0]]))
