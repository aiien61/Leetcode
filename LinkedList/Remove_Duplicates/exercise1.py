from __future__ import annotations
from base import Node, LinkedList
from typing import Set

#   +===================================================+
#   |                  WRITE THE CODE HERE             |
#   | Description:                                      |
#   | - This method removes all nodes with duplicate    |
#   |   values from the linked list.                    |
#   | - It keeps track of seen values with a set.       |
#   | - If a value is repeated, it is skipped over by   |
#   |   changing the 'next' pointer of the previous     |
#   |   node, effectively removing the duplicate.       |
#   | - The list's length is adjusted for each removed  |
#   |   duplicate.                                      |
#   |                                                   |
#   | Tips:                                             |
#   | - We maintain a 'previous' node as a reference    |
#   |   to re-link the list when skipping duplicates.   |
#   | - The 'current' node iterates through the list.   |
#   | - The 'values' set holds unique items seen so far.|
#   +===================================================+

class SolutionList(LinkedList):
    def remove_duplicates(self) -> None:
        if self.head is None:
            return None

        previous: Node = self.head
        current: Node = previous.next
        seen: Set[int] = {previous.value}

        while current is not None:
            if current.value in seen:
                previous.next = current.next
                current.next = None
                current = previous.next
            else:
                seen.add(current.value)
                current = current.next
                previous = previous.next
        return None
