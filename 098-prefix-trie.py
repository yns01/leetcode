class Trie:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_leaf_node = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        current_node = self.root
        for c in word:
            if c in current_node.children:
                current_node = current_node.children.get(c)
            else:
                n = self.Node()
                current_node.children[c] = n
                current_node = n

        current_node.is_leaf_node = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for c in word:
            n = current_node.children.get(c, None)
            if not n:
                return False

            current_node = n

        return current_node.is_leaf_node

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for c in prefix:
            n = current_node.children.get(c, None)
            if not n:
                return False

            current_node = n

        return True


t = Trie()
t.insert('app')
t.insert('apple')
t.insert('car')
print(t.search('appl'))
print(t.startsWith('c'))
