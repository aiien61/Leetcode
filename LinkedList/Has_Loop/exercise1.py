from __future__ import annotations
from base import Node, LinkedList

class SolutionList(LinkedList):
    def has_loop(self) -> bool:
        slow: Node = self.head
        fast: Node = self.head
        while True:
            if fast is None or fast.next is None:
                break
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
