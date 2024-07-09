import unittest
from typing import Optional

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


def find_kth_from_end(linked_list: LinkedList, k: int) -> Optional[Node]:
    slow = linked_list.head
    fast = linked_list.head
    for _ in range(k):
        if fast is None: return None
        fast = fast.next
    while True:
        if fast is None: break
        slow = slow.next
        fast = fast.next
    return slow


class Evaluate(unittest.TestCase):
    def test_empty_list(self):
        my_linked_list = LinkedList(1)
        my_linked_list.head = None
        my_linked_list.tail = None

        k = 2
        expected = None
        actual = find_kth_from_end(my_linked_list, k)
        if actual is not None:
            actual = actual.value
        self.assertEqual(expected, actual)

    def test_k_less_than_length(self):
        my_linked_list = LinkedList(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.append(4)
        my_linked_list.append(5)
        my_linked_list.append(6)


        k = 2
        expected = 5
        actual = find_kth_from_end(my_linked_list, k)
        if actual is not None:
            actual = actual.value

        self.assertEqual(expected, actual)

    def test_k_equal_to_length(self):
        my_linked_list = LinkedList(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.append(4)
        my_linked_list.append(5)
        my_linked_list.append(6)

        k = 1
        expected = 6
        actual = find_kth_from_end(my_linked_list, k)
        if actual is not None:
            actual = actual.value

        self.assertEqual(expected, actual)

    def test_k_more_than_length(self):
        my_linked_list = LinkedList(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.append(4)
        my_linked_list.append(5)
        my_linked_list.append(6)

        k = 10
        expected = None
        actual = find_kth_from_end(my_linked_list, k)
        if actual is not None:
            actual = actual.value

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()