class Node:
    def __init__(self, k=0, v=0):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        n = self.cache.get(key)
        self.__move_to_front(n)

        return n.v

    def __move_to_front(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.head.next
        node.next.prev = node

        self.head.next = node
        node.prev = self.head

    def __insert_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def __remove_back(self):
        key_removed = self.tail.prev.k
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        return key_removed

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            n = self.cache.get(key)
            n.v = value
            self.__move_to_front(n)
        else:
            n = Node(key, value)
            self.__insert_front(n)
            self.cache[key] = n

            if len(self.cache) > self.capacity:
                removed = self.__remove_back()
                del self.cache[removed]


c = LRUCache(2)
c.put(1, 1)
c.put(2, 2)
print(c.get(1))
c.put(3, 3)
print(c.get(2))
c.put(4, 4)
print(c.get(1))
print(c.get(3))
print(c.get(4))
# [null,null,null,1,null,-1,null,-1,3,4]
