import unittest
from exercise1 import SolutionList
from typing import List

def linkedlist_to_list(head):
    result = []
    while head is not None:
        result.append(head.value)
        head = head.next
    return result

class TestReverse(unittest.TestCase):
    def test_reverse_when_multiple_nodes(self):
        ll = SolutionList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)

        ll.reverse()

        expected = [5, 4, 3, 2, 1]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_reverse_when_single_node(self):
        ll = SolutionList(1)

        ll.reverse()

        expected = [1]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_reverse_when_list_is_empty(self):
        ll = SolutionList(None)
        ll.head = None
        ll.tail = None
        ll.length = 0

        ll.reverse()

        expected = []
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_reverse_when_two_node(self):
        ll = SolutionList(1)
        ll.append(2)

        ll.reverse()

        expected = [2, 1]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()