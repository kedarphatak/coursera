def deleteDuplicatesEntirely(A):
    """
    Delete all duplicate elements from linked list.
    e.q. Ip: 1->2->2->2->3->4->4->5 Op: 1->3->5
    trick: Use 2 pointers one to check for duplicates and one for keeping track
    of elements before duplicates start.
    """
    p = A
    head = q = ListNode(None)
    head.next = p
    while p is not None and p.next is not None:
        if p.val == p.next.val:
            while p is not None and p.next is not None and (p.val == p.next.val):
                p = p.next
            p = p.next
            q.next = p
        else:
            q = q.next
            p = p.next

    return head.next


def deleteOnlyDuplicates(A):
    """
    Delete only duplicate but keep one instance of duplicated element.
    e.g. Ip: 1->2->2->2->3->4->4->5 Op: 1->2->3->4->5
    """
    p = A
    while p is not None and p.next is not None:
        if p.val == p.next.val:
            q = p.next.next
            p.next = q
            if q is None:
                break
        else:
            p = p.next
    return A
