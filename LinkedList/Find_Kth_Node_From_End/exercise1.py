from typing import Optional
from base import Node, LinkedList


def find_kth_from_end(linked_list: LinkedList, k: int) -> Optional[Node]:
    slow = linked_list.head
    fast = linked_list.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while True:
        if fast is None:
            break
        slow = slow.next
        fast = fast.next
    return slow
