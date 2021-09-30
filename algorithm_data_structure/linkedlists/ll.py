class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next


class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size

    def add_node(self, data):
        new_node = Node(data, next=self.root)
        self.root = new_node
        self.size += 1

    def delete(self, data):
        this_node = self.root
        prev_node = None
        while this_node is not None:
            if this_node.get_data() == data:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
        
    def find(self, data):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == data:
                return data
            elif this_node.get_next() is None:
                return False
            else:
                this_node = this_node.get_next()

    def print_nodes(self):
        this_node = self.root
        while this_node is not None:
            print this_node.get_data()
            this_node = this_node.get_next()

    def reverse_iterative(self):
        prev = None
        current = self.root
        while current is not None:
            nxt = current.get_next()
            current.next = prev
            prev = current
            current = nxt
        self.root = prev
