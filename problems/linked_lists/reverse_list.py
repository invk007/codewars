from problems.linked_lists.list import ListNode, from_array_to_list


def reverse_list(head: ListNode[int]) -> ListNode[int]:
    previous_node: ListNode[int] | None = None
    current_node = head

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node


if __name__ == '__main__':
    l = from_array_to_list([1, 2, 3, 4, 5])
    print(l)
    reversed_l = reverse_list(l)
    print(reversed_l)
