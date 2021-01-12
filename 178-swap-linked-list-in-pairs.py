class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None

        current = head
        if not current.next:
            return head

        dummy = ListNode(0)
        last = dummy

        while current and current.next:
            nxtnxt = current.next.next

            curr = current.next
            prev = current

            curr.next = prev
            prev.next = nxtnxt

            last.next = curr
            last = last.next.next

            current = nxtnxt

        return dummy.next


def prettyPrintLinkedList(node):
    while node and node.next:
        print(str(node.val) + "->", end='')
        node = node.next

    if node:
        print(node.val)
    else:
        print("Empty LinkedList")


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
prettyPrintLinkedList(Solution().swapPairs(head))
