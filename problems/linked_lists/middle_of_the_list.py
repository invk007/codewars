from problems.linked_lists.list import ListNode, from_array_to_list


def solution(head: ListNode[int]) -> ListNode[int]:
    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    result = solution(from_array_to_list(arr))
    print(result)
