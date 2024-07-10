from base import Node, DoublyLinkedList


class SolutionList(DoublyLinkedList):
    def reverse(self) -> None:
        self.head, self.tail = self.tail, self.head
        temp: Node | None = self.head
        while temp is not None:
            temp.next, temp.prev = temp.prev, temp.next
            temp = temp.next
        return None
