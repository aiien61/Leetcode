import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = temp
        while temp.next is not None:
            prev = temp
            temp = temp.next
        prev.next = None
        self.tail = prev
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    
    def has_loop(self):
        slow = self.head
        fast = self.head
        while True:
            if fast is None or fast.next is None:
                break
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
class Evaluate(unittest.TestCase):
    def test_has_loop(self):
        my_linked_list_1 = LinkedList(1)
        my_linked_list_1.append(2)
        my_linked_list_1.append(3)
        my_linked_list_1.append(4)
        my_linked_list_1.tail.next = my_linked_list_1.head
        self.assertTrue(my_linked_list_1.has_loop())

        my_linked_list_2 = LinkedList(1)
        my_linked_list_2.append(2)
        my_linked_list_2.append(3)
        my_linked_list_2.append(4)
        my_linked_list_2.append(5)
        my_linked_list_2.append(6)
        my_linked_list_2.tail.next = my_linked_list_2.head.next.next.next  # 6 -> 4
        self.assertTrue(my_linked_list_2.has_loop())

    def test_has_no_loop(self):
        my_linked_list_3 = LinkedList(1)
        my_linked_list_3.append(2)
        my_linked_list_3.append(3)
        my_linked_list_3.append(4)
        self.assertFalse(my_linked_list_3.has_loop())
    
    def test_no_nodes(self):
        my_linked_list_4 = LinkedList(1)
        my_linked_list_4.pop()
        self.assertFalse(my_linked_list_4.has_loop())
