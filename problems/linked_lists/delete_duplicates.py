from problems.linked_lists.list import ListNode, from_array_to_list


def solution(head: ListNode[int]) -> ListNode[int]:
    current = head

    while current and current.next:
        while current.next and current.val == current.next.val:
            current.next = current.next.next
        current = current.next

    return head

if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    result = solution(from_array_to_list(arr))

    while result:
        print(result.val)
        result = result.next
