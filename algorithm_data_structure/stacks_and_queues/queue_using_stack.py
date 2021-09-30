from stack import Stack


class QueueFromStack:
    def __init__(self):
        self._en_q = Stack()
        self._de_q = Stack()
        self.size = 0

    def enqueue(self, element):
        self._en_q.push(element)
        self.size += 1

    def dequeue(self):
        if self._de_q.isEmpty():
            while not self._en_q.isEmpty():
                self._de_q.push(self._en_q.pop())
        self.size -= 1
        return self._de_q.pop()

    def isEmpty(self):
        if self._en_q.isEmpty() and self._de_q.isEmpty():
            return True
        return False

    def getSize(self):
        return self.size


def main():
    qs = QueueFromStack()
    print qs.isEmpty()
    for i in range(3):
        qs.enqueue(i)
    print qs.getSize()
    while not qs.isEmpty():
        print "Dequeuing {}".format(qs.dequeue())
    print qs.getSize()


if __name__ == "__main__":
    main()
