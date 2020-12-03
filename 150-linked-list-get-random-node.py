from random import randint


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        count = 0
        current = self.head
        candidate = None

        while current:
            count += 1
            if randint(0, count-1) == 0:
                candidate = current

            current = current.next

        return candidate.val


class Solutionv1:
    def __init__(self, head: ListNode):
        self.index = []
        while head:
            self.index.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return self.index[randint(0, len(self.index) - 1)]
