from dataclasses import dataclass
from http.cookiejar import cut_port_re
from typing import Optional, TypeVar


@dataclass
class ListNode[T]:
    val: T
    next: Optional['ListNode'] = None


    def __str__(self) -> str:
        current = self
        result = ""

        while current:
            result += f"{current.val} "
            current = current.next

        return result


T = TypeVar("T")


def from_array_to_list(arr: list[T]) -> ListNode[T]:
    head = ListNode(val=arr[0])
    prev = head
    for i in arr[1:]:
        new_node = ListNode(val=i, next=None)
        prev.next = new_node
        prev = new_node

    return head

def from_list_to_array(head: ListNode[T] | None) -> list[T]:
    result = []
    if head is None:
        return result
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


if __name__ == '__main__':
    test_list = from_array_to_list([1, 2, 3, 4, 5])

    current = test_list

    while current:
        print(current.val)
        current = current.next
