from ll import Node, LinkedList
from merge_sorted_ll import print_nodes


def reverse_iterative(l1):
    """
    Reverse linkedlist using iterative method

    :param l1: root of linkedlist
    :return: l1: root of reversed linkedlist
    """
    current_node = l1
    prev = None
    while current_node is not None:
        nxt = current_node.get_next()
        current_node.set_next(prev)
        prev = current_node
        current_node = nxt
    l1 = prev
    return l1


def reverse_between(head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    # Special case when m == n return LL as is
    if m == n:
        return head
    # Initialize counter
    cnt = 1
    current = head
    prev = None
    # Find a node before m and after n
    while current is not None:
        if cnt == m:
            before_m = prev
            chunk_ll = current
        elif cnt == n:
            after_n = current.next
            # After n terminate LL
            current.next = None
            break
        cnt += 1
        prev = current
        current = current.next

    # Reverse chunk of LL from m to n
    c = chunk_ll
    prev = None
    while c is not None:
        nxt = c.next
        c.next = prev
        prev = c
        c = nxt
    chunk_ll = prev

    # Traverse reversed LL from m to n and join after_n node at the end
    c = chunk_ll
    while c is not None:
        if c.next is None:
            c.next = after_n
            break
        c = c.next
    
    if before_m is None:
        # If before_m is None return LL as is.
        return chunk_ll
    else:
        # If before_m is not None that means before part exist so join it to chunk_ll as prefix
        before_m.next = chunk_ll
        return head

def main():
    l1 = LinkedList()
    for i in [100, 80, 60, 40, 20, 0]:
        l1.add_node(i)
    print "l1:"
    print_nodes(l1.root)
    l1_reversed = reverse_iterative(l1.root)
    print "l1_reversed:"
    print_nodes(l1_reversed)
    print "Reverse LinkedList from node no 2 to node 4"
    l1 = LinkedList()
    for i in [100, 80, 60, 40, 20, 0]:
        l1.add_node(i)
    l1_reversed = reverse_between(l1.root, 2, 4)
    print_nodes(l1_reversed)


if __name__ == '__main__':
    main()  
