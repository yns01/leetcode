from collections import Counter
from typing import List


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.frequencies = Counter()
        self.index = {}
        self.uniq_head = ListNode(0)
        self.uniq_tail = ListNode(0)

        self.uniq_head.next = self.uniq_tail
        self.uniq_tail.prev = self.uniq_head

        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        if not self.index:
            return -1

        return self.uniq_head.next.val

    def add(self, value: int) -> None:
        if value in self.frequencies:
            # We only need to remove value from the list.
            # This occurs when we add value three times.
            # First time, it will be added to the last, then removed
            # finally we should not do any operations on the list
            node = self.index.get(value, None)
            if node:
                node.next.prev = node.prev
                node.prev.next = node.next

                del self.index[value]

        else:
            node = ListNode(value)

            node.prev = self.uniq_tail.prev
            node.next = self.uniq_tail

            self.uniq_tail.prev.next = node
            self.uniq_tail.prev = node

            self.index[value] = node
            self.frequencies[value] = 1


sol = FirstUnique([7, 7, 7, 7, 7, 7])
print(sol.showFirstUnique())  # -1
sol.add(7)
sol.add(3)
sol.add(3)
sol.add(7)
sol.add(17)
print(sol.showFirstUnique())  # 17
