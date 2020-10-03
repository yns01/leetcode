class WordDictionary:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_leaf_node = False

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
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
        def recurse(node: self.Node, char_index: int):
            if char_index == len(word):
                return node.is_leaf_node

            if word[char_index] != '.':
                n = node.children.get(word[char_index], None)
                if not n:
                    return False

                char_index += 1
                return recurse(n, char_index)
            else:
                char_index += 1
                for c in node.children.values():
                    found = recurse(c, char_index)
                    if found:
                        return found

                return False

        return recurse(self.root, 0)


wd = WordDictionary()
wd.addWord('app')
wd.addWord('apple')
wd.addWord('car')
print(wd.search('ca.'))
