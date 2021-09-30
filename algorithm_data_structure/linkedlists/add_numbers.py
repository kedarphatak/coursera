from ll import Node, LinkedList
from merge_sorted_ll import print_nodes
from reverse_iterative import reverse_iterative

def add_numbers(l1, l2):
    """
    Add two numbers represented by LinkedList

    :param l1: root of linked list
    :param l2: root of linked list
    :return: sum_ll_root: root of linked list
    """
    l1 = reverse_iterative(l1)
    l2 = reverse_iterative(l2)
    sum_ll = LinkedList()
    carry = 0
    while l1 is not None and l2 is not None:
        sum = l1.get_data() + l2.get_data() + carry
        s = sum % 10
        carry = sum / 10
        print carry, s, l1.get_data(), l2.get_data(), carry
        sum_ll.add_node(s)
        l1 = l1.get_next()
        l2 = l2.get_next()
    if carry:
        sum_ll.add_node(carry)
    sum_ll_root = reverse_iterative(sum_ll.root)
    return sum_ll_root


def main():
    l1 = LinkedList()
    l2 = LinkedList()
    for i in reversed(range(1, 4)):
        l1.add_node(i)
    for i in reversed(range(6, 9)):
        l2.add_node(i)
    print "l1:"
    print_nodes(l1.root)
    print "l2:"
    print_nodes(l2.root)
    print "sum:"
    sum_ll_root = add_numbers(l1.root, l2.root)
    print_nodes(sum_ll_root)


if __name__ == "__main__":
    main()
