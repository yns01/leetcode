from random import randrange


class RandomizedSet:

    def __init__(self):
        self.index = {}
        self.data = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

        if val in self.index:
            return False

        self.data.append(val)
        self.index[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        if not val in self.index:
            return False

        element_pos = self.index.get(val)
        del self.index[val]

        # To remove, we swap the element to remove with the last one.

        # Swap the elements
        self.data[element_pos], self.data[-1] = self.data[-1], self.data[element_pos]

        # Remove the last element.
        self.data.pop()

        # Update the index
        if element_pos < len(self.data):
            self.index[self.data[element_pos]] = element_pos
        return True

    def getRandom(self) -> int:
        random_index = randrange(len(self.data))
        return self.data[random_index]


# ["RandomizedSet","remove","remove","insert","getRandom","remove","insert"]
# [[],[0],[0],[0],[],[0],[0]]

obj = RandomizedSet()
param_1 = obj.remove(0)
print(param_1)
param_1 = obj.remove(0)
print(param_1)
param_1 = obj.insert(0)
print(param_1)
param_1 = obj.remove(0)
print(param_1)
param_1 = obj.insert(0)
print(param_1)
