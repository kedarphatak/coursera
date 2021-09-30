class Queue():
    def __init__(self, elements=None):
        self._queue = []
        self.verbose = False
        if elements:
            for e in elements:
                self._queue.append(e)

    def enqueue(self, element):
        if element:
            if self.verbose:
                print "Adding {} to queue.".format(element)
            self._queue.append(element)

    def dequeue(self):
        if self._queue:
            if self.verbose:
                print "Removing {} from queue.".format(self._queue[0])
            return self._queue.pop(0)
        print "Queue is empty."
        return None

    def isEmpty(self):
        if self._queue:
            return False
        return True

    def printQ(self):
        for element in self._queue:
            print element


def main():
    q = Queue()
    print q.isEmpty()
    for i in range(10):
        q.enqueue(i)
    print q.isEmpty()
    while not q.isEmpty():
        q.dequeue()
    print q.isEmpty()


if __name__ == "__main__":
    main()
