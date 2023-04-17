from problems.linked_lists.list_node import ListNode


def list_to_linked_list(in_list: list[int]) -> ListNode:
    head = ListNode(val=in_list[0])
    dummy = head

    for el in in_list[1:]:
        next = ListNode(val=el)
        dummy.next = next
        dummy = next

    return head
