from base import Node, DoublyLinkedList

class SolutionList(DoublyLinkedList):
    def is_palindrome(self) -> bool:
        forward_node: Node | None = self.head
        backward_node: Node | None = self.tail
        while forward_node != backward_node:
            if forward_node.value != backward_node.value:
                return False

            if forward_node.prev == backward_node:
                break

            forward_node = forward_node.next
            backward_node = backward_node.prev
        return True
