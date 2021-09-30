from ll import Node, LinkedList
from merge_sorted_ll import print_nodes
from reverse_iterative import reverse_iterative


def is_palindrome(ll):
    p = ll
    q = ll
    while p is not None and q is not None:
        if q.get_next() is None:
            length = "odd"
            # start new linkedlist from next of p
            q = p.get_next()
            # Terminate LinkedList
            p.set_next(None)
            break
        elif q.get_next().get_next() is None:
            length = "even"
            # start new linkedlist from next of p
            q = p.get_next()
            # Terminate LinkedList
            p.set_next(None)
            break
        p = p.get_next()
        q = q.get_next().get_next()
    # Set p to original root of LinkedList
    p = ll
    # Reverse LinkedList
    p = reverse_iterative(p)
    # If LinkedList is of odd length then skip 1st node for comparison
    if length == 'odd':
        p = p.get_next()
    # Compare nodes one by one and return False if mismatch found
    while p is not None and q is not None:
        if p.get_data() != q.get_data():
            return False
        p = p.get_next()
        q = q.get_next()
    return True


def main():
    l1 = LinkedList()
    l2 = LinkedList()
    l3 = LinkedList()
    l4 = LinkedList()
    for i in ['a', 'b', 'c', 'b', 'a']:
        l1.add_node(i)
    for i in ['a', 'b', 'c', 'c', 'b', 'a']:
        l2.add_node(i)
    for i in ['a', 'b', 'c']:
        l3.add_node(i)
    for i in ['a', 'b', 'c', 'd']:
        l4.add_node(i)
    print "l1:"
    print_nodes(l1.root)
    print is_palindrome(l1.root)
    print "l2:"
    print_nodes(l2.root)
    print is_palindrome(l2.root)
    print "l3:"
    print_nodes(l3.root)
    print is_palindrome(l3.root)
    print "l4:"
    print_nodes(l4.root)
    print is_palindrome(l4.root)

if __name__ == '__main__':
    main()
