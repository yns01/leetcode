class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: ListNode, insertVal: int) -> 'Node':
        if not head:
            head = ListNode(insertVal)
            head.next = head
            return head

        prev, current = head, head.next
        while True:
            # Two cases:
            # 1. We're insert a value which is not the min/min. In that, case,
            # we need to find its position
            if prev.val <= insertVal <= current.val:
                break
            # The max or min value goes to the same place. Right when the value are not increasing anymore.
            # We also need to check if the value actually belong here as we may have not visited the full list yet.
            # In the case [3,4,1], 2: We will meet the end of the list (4->1) but we should not insert the value there.
            elif prev.val > current.val and (insertVal >= prev.val or insertVal <= current.val):
                break

            prev = current
            current = current.next

            # As soon as current reaches head, we have visited all the possible nodes.
            if current == head:
                break

        new_node = ListNode(insertVal, current)
        prev.next = new_node

        return head


head = ListNode(3)
four = ListNode(4)
one = ListNode(1)
head.next = four
four.next = one
one.next = head
head = Solution().insert(head, 2)
print(head.val, head.next.val, head.next.next.val, head.next.next.next.val)
