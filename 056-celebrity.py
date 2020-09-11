# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    graph = [
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1],
    ]

    graph = [[1, 0], [0, 1]]

    return graph[a][b]


class Solution:
    def findCelebrity(self, n: int) -> int:
        if not n:
            return -1

        for i in range(0, n):
            knows_one = False
            for j in range(0, n):
                if i == j:
                    continue

                if knows(i, j):
                    knows_one = True
                    break

            if not knows_one:
                is_celeb = True
                for k in range(0, n):
                    if i == k:
                        continue

                    if not knows(k, i):
                        is_celeb = False

                if is_celeb:
                    return i

        return -1


print(Solution().findCelebrity(2))
