from problems.linked_lists.list_node import ListNode


def revert_list(head: ListNode) -> ListNode:
    current = head
    prev = None

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev
