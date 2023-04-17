from problems.linked_lists.list_node import ListNode


def array_to_linked_list(in_list: list[int]) -> ListNode:
    head = ListNode(val=in_list[0])
    dummy = head

    for el in in_list[1:]:
        next = ListNode(val=el)
        dummy.next = next
        dummy = next

    return head


def linked_list_to_array(head: ListNode) -> list[int]:
    pointer = head
    result = []

    while pointer:
        result.append(pointer.val)
        pointer = pointer.next

    return result
