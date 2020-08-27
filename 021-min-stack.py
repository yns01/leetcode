class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        if not self.mins:
            self.mins.append(x)
            return

        if x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self) -> None:
        e = self.stack.pop()
        if self.mins[-1] == e:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


class MinStack2:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        current_min = self.getMin()
        if current_min is None or x < current_min:
            current_min = x

        self.stack.append((x, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None

        return self.stack[-1][1]


minStack = MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(0)
m = minStack.getMin()
print(m)
# // return -3
minStack.pop()
# // return 0
t = minStack.getMin()
print(t)
# // return -2
