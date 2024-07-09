import unittest
from base import Node, LinkedList
from exercise1 import find_kth_from_end

class Evaluate(unittest.TestCase):
    def test_find_kth_from_end_when_empty_list(self):
        ll = LinkedList(1)
        ll.head = None
        ll.tail = None

        k = 2
        expected = None
        actual = find_kth_from_end(ll, k)
        if actual is not None:
            actual = actual.value
        self.assertEqual(expected, actual)

    def test_find_kth_from_end_when_k_less_than_length(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        ll.append(6)

        k = 2
        expected = 5
        actual = find_kth_from_end(ll, k)
        if actual is not None:
            actual = actual.value

        self.assertEqual(expected, actual)

    def test_find_kth_from_end_when_k_equal_to_length(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        ll.append(6)

        k = 1
        expected = 6
        actual = find_kth_from_end(ll, k)
        if actual is not None:
            actual = actual.value

        self.assertEqual(expected, actual)

    def test_find_kth_from_end_when_k_more_than_length(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        ll.append(6)

        k = 10
        expected = None
        actual = find_kth_from_end(ll, k)
        if actual is not None:
            actual = actual.value

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
