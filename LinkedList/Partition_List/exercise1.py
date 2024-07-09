#   +===================================================+
#   |               WRITE THE CODE                      |
#   | Description:                                      |
#   | - The method partitions a linked list around a    |
#   |   value `x`.                                      |
#   | - It rearranges the nodes so that all nodes less  |
#   |   than `x` come before all nodes greater or equal |
#   |   to `x`.                                         |
#   |                                                   |
#   | Tips:                                             |
#   | - We use two dummy nodes, `dummy1` and `dummy2`,  |
#   |   to build two separate lists: one for elements   |
#   |   smaller than `x` and one for elements greater   |
#   |   or equal to `x`.                                |
#   | - `prev1` and `prev2` help us keep track of the   |
#   |   last nodes in these lists.                      |
#   | - Finally, we merge these two lists by setting    |
#   |   `prev1.next = dummy2.next`.                     |
#   | - The head of the resulting list becomes          |
#   |   `dummy1.next`.                                  |
#   +===================================================+

from base import Node, LinkedList

class SolutionList(LinkedList):
    def partition_list(self, x: int) -> None:
        if self.head is None:
            return None

        dummy1 = Node(None)
        dummy2 = Node(None)
        prev1 = dummy1
        prev2 = dummy2

        node = self.head
        while node is not None:
            if node.value < x:
                prev1.next = node
                prev1 = prev1.next
            else:
                prev2.next = node
                prev2 = prev2.next
            node = node.next

        # cut off original nodes' next pointers
        prev1.next = None
        prev2.next = None

        # merge
        prev1.next = dummy2.next

        # replace original list in place
        self.head = dummy1.next

        return None
