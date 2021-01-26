from collections import Counter, deque
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []

        # Sorted will first sort on ticket[0] then ticket[1]
        # So our neighbors will be sorted.
            # >>> sorted([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"]], key=lambda ticket: ticket[0])
            #  ['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL']]

            # >>> sorted([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"]])
            # ['JFK', 'ATL'], ['JFK', 'SFO'], ['SFO', 'ATL']]
        tickets = sorted(tickets)
        graph = {airport: [] for ticket in tickets for airport in ticket}

        for orig, dest in tickets:
            graph[orig].append(dest)

        seen, order = Counter((orig, dest) for orig, dest in tickets), []

        # Instead of marking the airport as seen, we mark the ticket. We do so
        # because we must use all the tickets and we may go trough the same
        # airport multiple times.
        def visit(node, parent):
            seen[(parent, node)] -= 1

            for nei in graph[node]:
                if seen[(node, nei)] >= 1:
                    visit(nei, node)

            order.append(node)

        visit('JFK', None)

        return list(reversed(order))

    def findItineraryv1(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []

        tickets = sorted(tickets)
        graph = {airport: deque() for ticket in tickets for airport in ticket}

        for from_, to in tickets:
            graph[from_].append(to)

        order = []

        # In this approach, we don't need a seen set as we remove the neighbors
        # as we visit them. We avoid infinite loops this way while making sure
        # we use all tickets. If we'd mark the city as seen, we would not be able
        # to visit it multiple times.
        # Note that we use a deque() as we want to visit neighbors in their sorted
        # order. deque() allows us to popleft() in O(1) time.
        # We can use a list, but we'd have to use pop() and reverse the sorting.
        def visit(node):
            neis = graph[node]
            while neis:
                visit(neis.popleft())

            order.append(node)

        visit('JFK')

        return list(reversed(order))


print(Solution().findItineraryv1(
    [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], [
      "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
