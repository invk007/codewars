
from problems.linked_lists.list import ListNode, from_array_to_list


def remove_nth_from_end(head: ListNode[int], n: int) -> ListNode[int] | None:
    slow = fast = head
    distance = 0

    base = ListNode(val=-1, next=head)
    prev = base

    while distance < n:
        fast = fast.next
        distance += 1

    while fast is not None:
        fast = fast.next
        prev = slow
        slow = slow.next

    prev.next = slow.next

    return base.next

if __name__ == '__main__':
    head = from_array_to_list([1, 2, 3, 4, 5])
    remove_nth_from_end(head, 2)
    print(head)
