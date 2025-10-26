from problems.linked_lists.list import ListNode, from_array_to_list


def solution(head: ListNode[int]) -> ListNode[int] | None:
    if head.next is None:
        return None
    slow = fast = head
    prev = slow

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next

    return head


if __name__ == '__main__':
    head = from_array_to_list([2,1])
    head = solution(head)
    print(head)
