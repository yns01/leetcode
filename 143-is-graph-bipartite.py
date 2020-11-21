from typing import List
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True

        # A graph is bipartite if and only if it is 2-colorable.
        # Try to color the graph using two colors. BFS is better approach
        # as it explore the graph layer by layer
        que, colors = deque(), {}

        # It might be a disconnect graph
        for n, _ in enumerate(graph):
            if n in colors:
                continue

            que.append(n)
            colors = {n: 'white'}

            while que:
                current_vertex = que.popleft()
                current_color = colors.get(current_vertex)
                neighbors = graph[current_vertex]

                # All the neighbors of the current vertex must have the alternate color
                # If we already visited it, we just enforce this check otherwise
                # we color it and then visit its neighbors.
                for nei in neighbors:
                    if not nei in colors:
                        colors[nei] = self.get_next_color(current_color)
                        que.append(nei)
                    elif colors.get(nei) == current_color:
                        return False

        return True

    def get_next_color(self, current_color):
        if current_color == 'black':
            return 'white'
        else:
            return 'black'


print(Solution().isBipartite(
    [[3], [7, 9], [], [0, 5], [], [3], [9], [1], [], [1, 6]]))

print(Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
