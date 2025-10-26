from problems.linked_lists.list import ListNode, from_array_to_list


def solution(head: ListNode[int], left: int, right: int) -> ListNode[int]:
    if left == right:
        return head

    i = j = 0
    dummy = ListNode(val=0, next=head)
    base = dummy
    current = head

    while i < left - 1:
        base = current
        current = current.next
        i += 1
        j += 1

    tail = current.next
    first = current

    while j < right - 1:
        next_node = tail
        tail = next_node.next
        next_node.next= current
        current = next_node
        j += 1

    base.next = current
    first.next = tail

    return dummy.next

if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    head = from_array_to_list(input_list)
    result = solution(head, 3, 4)
    print(head, result, sep="\n")
