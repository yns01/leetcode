class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return

        prev, curr = None, head
        count = 0
        while curr:
            count += 1

            if count == m:
                break

            prev = curr
            curr = curr.next

        con, tail = prev, curr
        prev = curr
        curr = curr.next

        while count <= n:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt

            count += 1

        if con:
            con.next = prev
        else:
            head = prev

        tail.next = curr

        return head


def printlist(node):
    if not node:
        print('none')
        return

    print(node.val)
    printlist(node.next)


a = ListNode(3)
b = ListNode(5)
# c = ListNode(2)
# d = ListNode(10)
# e = ListNode(1)
# f = ListNode(8)
# g = ListNode(6)
a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# f.next = g
printlist(a)
head = Solution().reverseBetween(a, 1, 2)
printlist(head)
