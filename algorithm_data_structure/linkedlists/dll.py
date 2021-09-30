class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

    def set_data(self, data):
        self.data = data

class DoublyLinkedList():
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add_node(self, data):
        new_node = Node(data, next=self.root)
        if self.root:
            print "Adding {} as a root.".format(data)
            self.root.set_prev(new_node)
        self.root = new_node
        self.size += 1

    def delete(self, data):
        current_node = self.root
        prev_node = None
        while current_node is not None:
            if current_node.get_data() == data:
                if current_node.get_prev() is None:
                    # Special case of deleting root node
                    self.root = current_node.get_next()
                else:
                    prev_node.set_next(current_node.get_next())
                if current_node.get_next() is not None:
                    current_node.get_next().set_prev(prev_node)
                self.size -= 1
                return True
            prev_node = current_node
            current_node = current_node.get_next()
        return False

    def printNode(self):
        current_node = self.root
        while current_node is not None:
            print current_node.get_data()
            current_node = current_node.get_next()

    def getSize(self):
        return self.size

    def reverse(self):
        prev = None
        current_node = self.root
        while current_node is not None:
            nxt = current_node.get_next()
            current_node.set_next(prev)
            prev = current_node
            current_node = nxt
            self.root = prev
        
 
def main():
    dll = DoublyLinkedList()
    for i in range(10):
        dll.add_node(i)
    print "Size of DLL:", dll.getSize()
    print "root node: ", dll.root.get_data()
    dll.printNode()
    dll.delete(9)
    print "Size of DLL:", dll.getSize()
    dll.printNode()
    print "Reverse DLL:"
    dll.reverse()
    dll.printNode()


if __name__ == '__main__':
    main()
