class Stack():
    def __init__(self, elements=None, verbose=False):
        self._stack = []
        self.verbose = verbose
        if elements:
            for e in elements:
                self._stack.append(e)

    def push(self, element):
        if self.verbose:
            print "pushing {} to stack.".format(element)
        if element is not None:
            self._stack.append(element)

    def isEmpty(self):
        if not self._stack:
            return True
        return False

    def pop(self):
        if not self.isEmpty():
            return self._stack.pop(-1)

    def top(self):
        return self._stack[-1]

    def printS(self):
        if self.verbose:
            print "printing from top"
        n = len(self._stack)
        for i in range(n - 1, -1, -1):
            print self._stack[i]


def main():
    s = Stack()
    print s.isEmpty()
    for i in range(10):
        s.push(i)
    print s.isEmpty()
    s.printS()
    while s.isEmpty():
        s.pop()
    print s.isEmpty()


if __name__ == "__main__":
    main()
