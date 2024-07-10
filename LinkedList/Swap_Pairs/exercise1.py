from base import Node, DoublyLinkedList


class SolutionList(DoublyLinkedList):
    def swap_pairs(self):
        if self.head is None:
            return None
        if self.length == 1:
            return None
        
        before = Node(None)
        before.next = self.head
        temp = self.head

        while temp is not None and temp.next is not None:
            left = temp.next
            right = temp.next.next

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
