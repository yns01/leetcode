from typing import List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result = ListNode(0)
        current = result

        # We add a counter value to be able to compare
        # two identical values
        # (5, 0, Node()) and (5, 1, Node())
        # Complexity in N log(k) with k the number of linked lists
        # Because at any point, we have at most k elements in the heap
        heap = []
        for counter, l in enumerate(lists):
            if not l:
                continue
            heapq.heappush(heap, (l.val, counter, l))

        while heap:
            val, counter, current_node = heapq.heappop(heap)
            nxt_result = ListNode(val)
            current.next = nxt_result
            current = nxt_result

            next_node = current_node.next if current_node else None
            if next_node:
                heapq.heappush(heap, (next_node.val, counter, next_node))

        return result.next
