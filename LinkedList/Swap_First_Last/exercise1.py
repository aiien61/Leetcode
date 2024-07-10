from base import Node, DoublyLinkedList

class SolutionList(DoublyLinkedList):
    def swap_first_last(self) -> None:
        if self.head is None:
            return None
        
        self.head.value, self.tail.value = self.tail.value, self.head.value
        return None
