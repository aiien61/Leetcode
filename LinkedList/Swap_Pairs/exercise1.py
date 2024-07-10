from base import Node, DoublyLinkedList


class SolutionList(DoublyLinkedList):
    def swap_pairs(self) -> None:
        if self.head is None:
            return None
        if self.length == 1:
            return None
        
        before: Node = Node(None)
        before.next = self.head
        temp: Node = self.head

        while temp is not None and temp.next is not None:
            left: Node = temp.next
            right: Node | None = temp.next.next

            # swap
            temp.prev = left
            temp.next = right

            # left node relinks
            left.prev = before
            left.next = temp
            before.next = left

            # right node relinks
            if right is not None:
                right.prev = temp

            # next iteration
            before = temp
            temp = temp.next

        self.head = self.head.prev
        return None
