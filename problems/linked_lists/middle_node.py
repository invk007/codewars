"""Given the head of a singly linked list, return the middle node of the linked
list. If there are two middle nodes, return the second middle node."""

import typing as t

from problems.linked_lists.list_node import ListNode


def middle_node(head: t.Optional[ListNode]) -> t.Optional[ListNode]:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
