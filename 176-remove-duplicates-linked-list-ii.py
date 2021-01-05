from collections import Counter


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        dummy = ListNode(0)
        last = dummy

        current = head
        while current:
            occurrences = 1
            base = current
            current = current.next
            while current and current.val == base.val:
                occurrences += 1
                current = current.next

            if occurrences == 1:
                last.next = base
                last = last.next

        last.next = None

        return dummy.next

    def deleteDuplicatesv1(self, head: ListNode) -> ListNode:
        if not head:
            return None

        frequencies = Counter()

        current = head
        while current:
            frequencies[current.val] += 1
            current = current.next

        dummy = ListNode(0)
        last = dummy

        current = head
        while current:
            f = frequencies[current.val]
            if f == 1:
                last.next = current
                last = current

            current = current.next

        last.next = None
        return dummy.next


def prettyPrintLinkedList(node):
    while node and node.next:
        print(str(node.val) + "->", end='')
        node = node.next

    if node:
        print(node.val)
    else:
        print("Empty LinkedList")


# [1,1,1,2,3]
prettyPrintLinkedList(Solution().deleteDuplicates(
    ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))))

prettyPrintLinkedList(Solution().deleteDuplicates(
    ListNode(1, ListNode(2, ListNode(2)))))

prettyPrintLinkedList(Solution().deleteDuplicatesv1(
    ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))))

prettyPrintLinkedList(Solution().deleteDuplicatesv1(
    ListNode(1, ListNode(2, ListNode(2)))))
