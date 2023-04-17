"""Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well."""

from problems.linked_lists.list_node import ListNode


def delete_duplicates(head: ListNode) -> ListNode:
    pointer = head

    while pointer and pointer.next:
        if pointer.val == pointer.next.val:
            pointer.next = pointer.next.next
        else:
            pointer = pointer.next

    return head
