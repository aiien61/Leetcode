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

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
    def find_middle_node(self):
        slow: Node = self.head
        fast: Node = self.head
        while True:
            if fast is None or fast.next is None:
                break
            slow = slow.next
            fast = fast.next.next
        return slow


class Evaluate(unittest.TestCase):
    def test_find_middle_node(self):
        my_linked_list = LinkedList(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.append(4)
        my_linked_list.append(5)
        expected = 3
        actual = my_linked_list.find_middle_node().value
        self.assertEqual(expected, actual)

        my_linked_list.append(6)
        expected = 4
        actual = my_linked_list.find_middle_node().value
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()