from base import Node, LinkedList

class SolutionList(LinkedList):
    def reverse_between(self, start_index: int, end_index: int) -> None:
        if self.head is None or self.length == 1:
            return None

        index: int = 0
        node: Node = self.head
        prev: Node = None

        while node is not None:
            if index == start_index:
                start_node: Node = node
                break
            prev = node
            node = node.next
            index += 1

        while node is not None:
            if index == end_index:
                end_node: Node = node
                break
            node = node.next
            index += 1

        reverse_node: Node = start_node
        while reverse_node != end_node:
            temp_node = reverse_node
            reverse_node = reverse_node.next
            temp_node.next = end_node.next
            end_node.next = temp_node

        if prev is not None:
            prev.next = end_node
        else:
            self.head = end_node
        return None
